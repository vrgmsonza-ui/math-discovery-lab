from pathlib import Path
import json
root=Path(__file__).parent
rows=json.loads((root/'dist/curriculum.json').read_text()); mapping={}
for g in range(1,11):
 for i,r in enumerate(x for x in rows if x['grade']==g):mapping[r['id']]={'grade':g,'cell':i,'focus':r['competencies'][0]}
assert len(mapping)==254
assert len({(m['grade'],m['cell']) for m in mapping.values()})==254
(root/'dist/thumbnails.js').write_text('const COMPETENCY_ART='+json.dumps(mapping,ensure_ascii=False,separators=(',',':'))+';\n')
print('254 unique competency-to-illustration assignments.')
