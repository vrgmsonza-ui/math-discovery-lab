const fs=require('fs'),vm=require('vm'),assert=require('assert');
const ctx=vm.createContext({console});vm.runInContext(fs.readFileSync(__dirname+'/dist/models.js','utf8')+fs.readFileSync(__dirname+'/dist/extensions.js','utf8')+';this.models=M;',ctx);let M=ctx.models,total=0;
for(const [id,m] of Object.entries(M)){const base=Object.fromEntries(m.controls.filter(c=>c.type!=='button').map(c=>[c.key,c.value]));let scenarios=[base];for(const c of m.controls){if(c.type==='range'||c.type==='number')scenarios.push({...base,[c.key]:c.min},{...base,[c.key]:c.max});if(c.type==='select')for(const v of c.options)scenarios.push({...base,[c.key]:v});}for(const s of scenarios){let r=m.render({...s});assert.equal(r.length,2,id);assert(!r[0].includes('NaN'),id+' invalid SVG');assert(!/="(?:Infinity|-Infinity)/.test(r[0]),id+' infinite coordinate');total++}}
function render(id,params){let m=M[id],s=Object.fromEntries(m.controls.filter(c=>c.type!=='button').map(c=>[c.key,c.value]));return m.render({...s,...params})[1]}
assert(render('right',{a:3,b:4}).includes('5'));assert(render('balance',{a:2,b:3,c:15,x:6}).includes('Solution x = (c − b) / a = 6'));
assert(render('fraction',{a:1,b:2,c:1,d:4,op:'Add'}).includes('0.75'));assert(render('fraction',{a:1,b:2,c:0,d:4,op:'Divide'}).includes('undefined'));
assert(render('sine',{A:30,a:6,b:10}).includes('Triangle 2'));assert(!render('sine',{A:30,a:5,b:10}).includes('Triangle 2')); assert(render('sine',{A:30,a:2,b:10}).includes('No triangle'));
assert(render('data',{data:'3,5,5,7,10'}).includes('mean = 6'));assert(render('data',{data:'-1,2',view:'Pie graph'}).includes('counts'));
assert(render('linear',{m:1,n:1,b:2,c:3,view:'Two lines'}).includes('no solution'));assert(render('quadratic',{a:0}).includes('Degenerate'));
assert(render('composite',{w:8,h:6,cutw:3,cuth:2}).includes('42 square units'));assert(render('composite',{w:8,h:6,cutw:3,cuth:2}).includes('28 units'));
assert(render('absolute',{h:2,k:-1}).includes('No solution'));assert(render('absolute',{h:2,k:0}).includes('One solution'));assert(render('absolute',{h:2,k:3}).includes('x = -1 or x = 5'));
assert(render('functions',{pairs:'1,2;1,3'}).startsWith('Not a function'));assert(render('functions',{pairs:'1,2;1,2'}).startsWith('Function'));
assert(render('radicals',{n:72,a:4,b:-3}).includes('Rejected'));assert(render('trianglecheck',{a:3,b:4,c:5}).includes('right triangle'));assert(render('trianglecheck',{a:1,b:2,c:3}).includes('No triangle'));
assert(render('scientific',{a:3,p:4,b:2,q:3,op:'×'}).includes('6 × 10<sup>7'));assert(render('scientific',{b:0,op:'÷'}).includes('Undefined'));
assert(render('statistics',{data:'1,2,3,4',score:2}).includes('37.5%'));assert(render('statistics',{data:'1,2,3,4'}).includes('mean deviation about mean = 1;'));
assert(render('pyramid',{shape:'Rectangle',a:4,b:3,h:6}).includes('24 cubic units'));
assert(render('blocks',{a:27,b:15,op:'Add'}).includes('4 tens and 2 ones'));assert(render('blocks',{a:32,b:15,op:'Subtract'}).includes('Trade 1 ten'));
const rows=JSON.parse(fs.readFileSync(__dirname+'/dist/curriculum.json'));assert.equal(rows.length,254);for(const r of rows){assert.equal(r.review.discussion.length,r.competencies.length);for(const m of r.models)assert(M[m],'Missing model '+m)}
for(let g=1;g<=10;g++)for(let t=1;t<=3;t++){let weeks=new Set;for(const r of rows.filter(r=>r.grade===g&&r.term===t)){let w=r.weeks.match(/\d+/g).map(Number);for(let i=w[0];i<=w.at(-1);i++)weeks.add(i)}assert.equal(weeks.size,10)}
console.log(`${Object.keys(M).length} models, ${total} rendering scenarios, numeric checks, and 300 curriculum week slots passed.`);
