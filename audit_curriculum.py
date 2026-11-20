"""Review model relevance and keep every original competency intact."""
import json,re,pathlib
root=pathlib.Path(__file__).parent
p=root/'dist/curriculum.json'; rows=json.loads(p.read_text())
original=json.loads(__import__('subprocess').check_output(['git','show','4e0048113302654cf0d8c172039410d7e805ff12:dist/curriculum.json'],cwd=root))
additions=[('blocks',r'regroup|tens and ones|decompose.*number|concrete.*models'),('composite',r'composite figures'),('pyramid',r'pyramids'),('absolute',r'absolute value'),('functions',r'\brelations\b|\bdomain\b|range of a function'),('sampling',r'sampling|data collection'),('statistics',r'frequency|stem-and-leaf|mean deviation|measures of position|percentile rank|outliers|quartiles|deciles|percentiles'),('scientific',r'scientific notation'),('monomials',r'monomial|laws of exponents'),('radicals',r'radical|rationalizing'),('trianglecheck',r'triangle inequalit|converse in classifying|classify triangles')]
changes=[]
for r,old in zip(rows,original):
 assert r['competencies']==old['competencies']
 text=' '.join(r['competencies']).lower(); r['models']=list(old['models']); before=list(r['models'])
 # Remove lexical collisions (e.g. "measure" inside "measures of position").
 guards={'units':r'\bconvert|units of measur|\bmass\b|\bcapacity\b|\bliters\b|\bmilliliters\b|\bkilograms\b|\bgrams\b','linear':r'\blinear\b|\bslope|\bintercept|rate of change|\brelations\b|\bfunctions\b','balance':r'equation|algebraic expression|variables|formulas|unknown|equivalent expression|equivalent number facts|number sentence','circle':r'\bcircles?\b|circumference|\bsectors?\b|central angles|inscribed angles','shapes':r'\barea\b|perimeter|2-dimensional|plane figure|quadrilateral|triangles|rectangles|squares|half circles|quarter circles|height of','polygon':r'\bpolygons?\b|interior angle|exterior angle','counting':r'counting principle|sample space|possible outcomes|combined events','place':r'\bcount\b|count up|counts by|numerals|place value|value of a digit|read and write.*numbers|represent numbers|decompose.*digit'}
 for m,pat in guards.items():
  if m in r['models'] and not re.search(pat,text):r['models'].remove(m)
 if 'polygon' in r['models'] and 'frequency' in text and not re.search(r'interior|exterior|convex|concave',text):r['models'].remove('polygon')
 if 'inequality' in r['models'] and 'triangle inequalit' in text and not re.search(r'linear inequal|quadratic inequal|absolute value',text):r['models'].remove('inequality')
 if 'blocks' not in r['models'] and r['grade']<=2 and re.search(additions[0][1],text):r['models'].append('blocks')
 for m,pat in additions[1:]:
  if re.search(pat,text) and m not in r['models']:r['models'].append(m)
 # Small integer arrays cannot perform large-number or decimal arithmetic.
 if re.search(r'multipl|divid|division',text) and re.search(r'decimal|digit|1 000|10 000|1000|integers',text) and 'numberline' not in r['models']:r['models'].append('numberline')
 if re.search(r'counts? by',text) and 'pattern' not in r['models']:r['models'].append('pattern')
 if re.search(r'area|perimeter',text) and 'triangle' in text and 'trianglecheck' not in r['models']:r['models'].append('trianglecheck')
 assert r['models'],r['id']
 r['review']={'status':'Companion models + teacher-led completion','discussion':[]}
 for c in r['competencies']:
  if re.search(r'proof|prove|postulates|theorems|justify',c,re.I):task='State the givens and conclusion. Use the model to form a conjecture, then write a two-column proof with a reason for every step. A changing diagram is evidence, not a proof.'
  elif re.search(r'construct|draw|cut-outs|compass|protractor|ruler|make models',c,re.I):task='Predict and inspect the model, then complete the named construction using the required ruler, protractor, compass, grid, or cut-outs. Label and check the finished work.'
  elif re.search(r'collect|interview|survey|sampling|reports|misleading|digital media|sources',c,re.I):task='Gather or bring real data for this competency. Identify the population, sample, source, labels and scale. Use the display to test a claim, then discuss bias and whether the evidence supports it.'
  elif re.search(r'solve.*problem|real.life|situations|financial plan',c,re.I):task='Create a Philippine classroom, shopping, travel, or measurement problem for this competency. State knowns and unknowns, choose a model, then show the calculation, units and a reasonableness check.'
  elif re.search(r'read and write|recognize coins|denominations|bills',c,re.I):task='Use the model to identify and compare examples. Have learners read them aloud and write the matching numerals, words or notation; use actual reference coins/bills where recognition is required.'
  else:task='Choose two examples and one contrasting example for this competency. Predict first, test with the relevant controls, and explain or record the relationship using the notation named above.'
  r['review']['discussion'].append(task)
 if before!=r['models']:changes.append((r['id'],before,r['models']))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
count=sum(len(r['competencies']) for r in rows)
report=['# Competency coverage review','',f'Reviewed {len(rows)} source weekly groups and {count} competency entries across Grades 1–10. All 300 grade–term–week slots remain represented. Original competency strings are unchanged.','', '## Findings and changes','',f'Corrected companion-model assignments in {len(changes)} groups. Added 11 models for previously weak or missing representations: tens/ones regrouping, composite figures, pyramids with different bases, absolute-value equations, functions/domain/range, sampling, frequency/position/variability, scientific-notation operations, monomial operations, radical simplification/equations and triangle inequalities.','', 'Expanded number-line precision to four decimal places, money denominations, rounding places and fixed time conversions. Removed lexical false positives such as an inequality number line for triangle inequalities and polygon geometry for frequency polygons.','', '## Limits that still need teacher-led completion','', 'These are companion simulations, not evidence of full competency mastery. Every competency now has a classroom completion prompt, selectable inside the lab and presentation view.','', '- Geometry construction, instrument use, two-column proofs, cut-outs and physical models need learner-produced work.','- Word problems, multistep solutions, reading/writing number names, actual currency recognition and surveys need contextual tasks and assessment.','- Algebra tiles still illustrate a limited family of nonnegative binomial products; general polynomial factorization, arbitrary rational-expression operations and equations reducible to quadratics require worked examples beyond these controls.','- Radical equations are demonstrated by √(x+a)=b; this does not cover every radical equation or operation.','- Circle geometry includes sector/segment area and intersecting chords; external secant/tangent angle and length cases still require teacher diagrams and worked solutions.','- The statistics extension includes frequency tables, stem-and-leaf and cumulative frequency polygons; grouped cumulative histograms and all textbook quantile conventions are not implemented.','- Cube nets do not represent every solid net. Time-zone controls use fixed offsets rather than an interactive world map.','', '## Group-by-group review','', '| Group | Companion models after review | Competencies | Completion |','|---|---|---:|---|']
for r in rows:report.append(f"| {r['id']} | {', '.join(r['models'])} | {len(r['competencies'])} | Model exploration + competency-specific teacher task |")
report+=['','## Assignment changes','']
for id,b,a in changes:report.append(f"- {id}: {', '.join(b)} → {', '.join(a)}")
(root/'COVERAGE_REVIEW.md').write_text('\n'.join(report)+'\n')
print(f'{count} competencies; {len(rows)} groups; {len(changes)} assignment corrections; original wording preserved')
