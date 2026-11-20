"""Compare source PDF bullet counts/order/opening wording with the retained curriculum."""
from pathlib import Path
import json,re,sys
root=Path(__file__).parent
source=Path(sys.argv[1]) if len(sys.argv)>1 else root.parent/'extracted'
rows=json.loads((root/'dist/curriculum.json').read_text());count=0
for grade in range(1,11):
 text=next(source.glob('[[]G'+str(grade)+']*.txt')).read_text()
 text=re.sub(r'Page \d+ of \d+\s*Last updated April 17, 2026','',text)
 text=re.sub(r'`?\s*Budget of Work\s*Grade \d+\s*\|\s*Mathematics','',text)
 parts=re.split(r'Learning Competenc(?:y|ies)\s*\n',text)[-3:]
 assert len(parts)==3
 for term,part in enumerate(parts,1):
  part=re.split(r'(?:Second|Third) Term\s*\n',part)[0]
  bullets=part.split('●')[1:]
  entries=[c for r in rows if r['grade']==grade and r['term']==term for c in r['competencies']]
  assert len(bullets)==len(entries),(grade,term)
  norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
  for a,b in zip(bullets,entries):
   assert norm(a).startswith(norm(b)[:65]),(grade,term,b)
   count+=1
print(f'{count} source bullets verified by count, order and opening wording across all 30 terms.')
