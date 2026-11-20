from pathlib import Path
import html,json
root=Path(__file__).parent
rows=json.loads((root/'dist/curriculum.json').read_text())
summary=(root/'COVERAGE_REVIEW.md').read_text().split('## Group-by-group review')[0]
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Competency coverage review | Math Discovery Lab</title><style>body{max-width:1100px;margin:40px auto;padding:20px;font:18px/1.6 system-ui;color:#173d39;background:#f8faf8}table{border-collapse:collapse;width:100%}td,th{border:1px solid #b9ccc0;padding:10px;text-align:left}a{color:#196859}h1,h2{line-height:1.2}</style><a href="./">Return to simulations</a>'
for line in summary.splitlines():
 if line.startswith('## '):page+='<h2>'+html.escape(line[3:])+'</h2>'
 elif line.startswith('# '):page+='<h1>'+html.escape(line[2:])+'</h1>'
 elif line:page+='<p>'+html.escape(line)+'</p>'
page+='<h2>All source groups</h2><p>All 506 source bullets were checked by count, order and opening wording across 30 grade-term sections. This confirms that entries are represented, not that every skill is fully simulated.</p><table><tr><th>Grade / Term / Week</th><th>Competencies</th><th>Companion models</th></tr>'
for r in rows:page+=f'<tr><td>{r["grade"]} / {r["term"]} / {r["weeks"]}</td><td>'+html.escape(' • '.join(r['competencies']))+'</td><td>'+html.escape(', '.join(r['models']))+'</td></tr>'
(root/'dist/coverage-review.html').write_text(page+'</table></html>')
