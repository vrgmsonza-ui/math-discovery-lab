import json,re,pathlib
p=pathlib.Path(__file__).parent/'dist/curriculum.json'
rows=json.loads(p.read_text())
rules=[
('sine',r'ambiguous'),('triangle',r'laws? of (?:sines|cosines)|oblique|bearings'),
('chords',r'chords|secant|tangent segments'),('circlegraph',r'equation of a circle|equations? of a circle|center.radius|radius of a circle from|graph of a circle'),
('circle',r'circumference|parts of a circle|areas? of (?:a )?circle|sectors?|segments of a circle|central angles|inscribed angles|draw circles|value of pi'),
('inequality',r'inequalit|absolute value equations'),('quadratic',r'quadratic|parabola|discriminant'),
('rational',r'rational algebraic|radical equations'),('polynomial',r'monomial|binomial|polynomial|special products'),
('geometry',r'congruen|proof|prove |postulates|theorems|parallelograms|trapezoids and kites|midline|bisector'),
('right',r'pythagorean|trigonometric|right triangles|special triangles|triangle similarity|angles of elevation|angles of depression|similarity'),
('polygon',r'polygons|interior angle|exterior angle'),('angle',r'\bangles\b|parallel|perpendicular|line segment|point, line|points, lines'),
('tessellation',r'tessellat'),('transform',r'translation|reflection|rotation|symmetr|slide|half turn|quarter turn|clockwise'),
('nets',r'nets'),('solid',r'volume|cubic|cu\. cm|solid|prisms|pyramids|cones|spheres|surface area'),
('shapes',r'2-dimensional|plane figure|quadrilateral|triangles|rectangles|squares|perimeter|areas? of|area,|height of|circle[s,]|half circles|quarter circles'),
('coordinates',r'cartesian|coordinates|midpoint|distance between two points|plot points'),
('linear',r'linear|slopes?|intercepts|rate of change|relations|functions'),
('balance',r'unknown|equation|algebraic expression|variables|formulas|properties of equality|equivalent expression|equivalent number facts'),
('variation',r'variation'),('powers',r'exponen|square roots|cube roots|radical|scientific notation|irrational'),
('interest',r'interest|depreciation'),('budget',r'financial plan|financial problems|profit|loss|discount|commission|sales tax|percentage increase|percentage decrease'),
('rate',r'uses of rates|involving rates|speed|best buy|instalment'),
('sets',r'sets|subsets|venn|union|intersection|conditional probability|complementary|mutually exclusive|dependent and independent'),
('counting',r'counting principle|sample space|possible outcomes|combined events'),
('probability',r'probabilit|experiments|likely|certain|impossible|compound events'),
('data',r'data|graphs|pictograph|central tendency|variability|measures of position|quartiles|percentile|box.and.whisker|frequency|statistical'),
('calendar',r'calendar|days of the week|months of the year|days and/or weeks'),
('clock',r'clock|time zones|elapsed time|timetables|12.hour|24.hour|involving time|read and write time'),
('units',r'convert.*units|conversion of units|units of measure|mass|capacity|liters|milliliters|kilograms|grams|sq\. cm to sq\. m'),
('length',r'length|distance|non.standard units'),
('money',r'money|coins|bills|peso|currency'),
('percent',r'percent|decimal.*fractions|fractions.*decimal'),
('ratio',r'ratio|proportion'),('fraction',r'fraction|halves|quarters|1/2|1/4|rational numbers'),
('factors',r'factors|multiples|divisibility|prime|composite numbers|gcf|lcm|even and odd'),
('pattern',r'pattern|sequence|next term'),('ordinal',r'ordinal|position of objects'),('round',r'round|estimate the sum|estimate the difference'),
('arrays',r'multipl|division|divide|groups|arrays|equal sharing'),('expression',r'mdas|gemdas|gmdas|order of operations|different operations'),
('numberline',r'add|subtract|compare.*numbers|order.*numbers|integers|number line|operations on rational'),
('place',r'count|numerals|place value|value of a digit|represent.*numbers|read and write.*numbers|decompose.*digit|tens and ones')]
for i,row in enumerate(rows):
 text=' '.join(row['text'].split('●')[1:]).lower();models=[]
 for id,pat in rules:
  if re.search(pat,text) and id not in models: models.append(id)
 # Limit broad lexical collisions, keeping explicit subject models.
 if row['grade']>=8 and 'shapes' in models and not re.search(r'perimeter|area|quadrilateral|rectangle|square|trapezoid|parallelogram',text):models.remove('shapes')
 if 'data' in models and not re.search(r'data|pictograph|statistic|quartile|percentile|frequency|bar graph|line graph|pie graph|box.and.whisker',text):models.remove('data')
 if 'ratio' in models and not re.search(r'\bratio\b|\bratios\b|\bproportion\b',text):models.remove('ratio')
 if 'arrays' in models and not re.search(r'multipl|division|divide|equal group|equal sharing',text):models.remove('arrays')
 if 'length' in models and row['grade']>3:models.remove('length')
 if 'money' in models and row['grade']>=7:models.remove('money')
 if 'numberline' in models and row['grade']>=8 and not re.search(r'integers|rational numbers|number line',text):models.remove('numberline')
 if not models: print('UNMATCHED',row);models=['numberline']
 row['models']=models;row['id']=f"g{row['grade']}-t{row['term']}-w{row['weeks'].replace(' to ','-')}-{i}"
 row['competencies']=[x.strip() for x in row['text'].split('●')[1:]]
 row['source']='[G'+str(row['grade'])+'] Mathematics — Three-Term Budget of Work, updated April 17, 2026'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for g in range(1,11):
 for t in range(1,4):
  covered=set()
  for r in rows:
   if (r['grade'],r['term'])==(g,t):
    w=list(map(int,re.findall(r'\d+',r['weeks'])));covered.update(range(w[0],w[-1]+1))
  assert covered==set(range(1,11)),(g,t,covered)
print('Validated all 300 grade/term/week slots across',len(rows),'source groups')
