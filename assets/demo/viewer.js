import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
const config=JSON.parse(document.getElementById('demo-data').textContent);
const data=config.parts;
import {toCreasedNormals} from 'three/addons/utils/BufferGeometryUtils.js';
const colors=config.palette.map(c=>[c.name,c.hex]);
const host=document.querySelector('#viewport'),status=document.querySelector('#status'),select=document.querySelector('#palette');
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0x000000,0);renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.05;host.append(renderer.domElement);
const scene=new THREE.Scene();scene.add(new THREE.HemisphereLight(0xf4f8ff,0x67758b,2.4));
for(const [pos,power] of [[[100,-180,230],2.8],[[-160,-80,100],1.3],[[10,180,200],2]]){const l=new THREE.DirectionalLight(0xffffff,power);l.position.set(...pos);scene.add(l)}
const camera=new THREE.PerspectiveCamera(30,1,.1,1500);camera.up.set(0,0,1);camera.position.set(160,-360,155);
const controls=new OrbitControls(camera,renderer.domElement);controls.target.set(0,0,82);controls.enableDamping=true;controls.minDistance=160;controls.maxDistance=700;controls.enablePan=true;controls.update();
const decode=(s,Type)=>{const raw=atob(s),bytes=new Uint8Array(raw.length);for(let i=0;i<raw.length;i++)bytes[i]=raw.charCodeAt(i);return new Type(bytes.buffer)};

const parts=data.map(d=>{const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(decode(d.positions,Float32Array),3));g.setIndex(new THREE.BufferAttribute(decode(d.indices,Uint32Array),1));g.computeVertexNormals();g.computeBoundingBox();const mesh=new THREE.Mesh(toCreasedNormals(g,Math.PI/4),new THREE.MeshStandardMaterial({color:colors[d.color][1],roughness:.68,metalness:0}));mesh.name=d.name;scene.add(mesh);return {mesh,color:d.color,expanded:new THREE.Vector3(...d.exploded_mm),from:new THREE.Vector3(),to:new THREE.Vector3(),fromOpacity:1,toOpacity:1}});
let mode='assembled',color='all',transitionStart=performance.now(),animating=false;const duration=950;
for(const [i,c]of colors.entries()){const o=document.createElement('option');o.value=String(i);o.textContent=c[0];select.append(o)}
function updateList(){
 const tbody=document.querySelector('#parts');tbody.replaceChildren();
 colors.forEach((c,i)=>{if(color!=='all'&&String(i)!==color)return;
 const members=parts.filter(p=>p.color===i),row=document.createElement('tr'),cell=document.createElement('td'),count=document.createElement('td');
 const dot=document.createElement('span');dot.className='dot';dot.style.background=c[1];
 const title=document.createElement('strong');title.textContent=c[0];
 const names=document.createElement('span');names.className='names';names.textContent=members.map(p=>p.mesh.name).join(', ');
 cell.append(dot,title,document.createElement('br'),names);count.textContent=members.length;row.append(cell,count);tbody.append(row);
 });
 const count=parts.filter(p=>color==='all'||String(p.color)===color).length;
 status.textContent=`${mode==='assembled'?'Assembled':'Exploded'} · ${color==='all'?'All colors':colors[Number(color)][0]} · ${count} ${count===1?'part':'parts'}`;
 document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===mode)));
}
function transition(){const now=performance.now();step(now);for(const p of parts){p.from.copy(p.mesh.position);p.to.copy(mode==='exploded'?p.expanded:new THREE.Vector3());p.fromOpacity=p.mesh.material.opacity;p.toOpacity=color==='all'||String(p.color)===color?1:0;p.mesh.visible=p.fromOpacity>.001||p.toOpacity>0;p.mesh.material.transparent=true;p.mesh.material.depthWrite=p.fromOpacity===1&&p.toOpacity===1}transitionStart=now;animating=true;updateList()}
function step(now){if(!animating)return;const t=Math.min(1,Math.max(0,(now-transitionStart)/duration)),e=t*t*(3-2*t);for(const p of parts){p.mesh.position.lerpVectors(p.from,p.to,e);const m=p.mesh.material;m.opacity=THREE.MathUtils.lerp(p.fromOpacity,p.toOpacity,e);p.mesh.visible=m.opacity>.001;if(t===1){m.transparent=p.toOpacity<1;m.depthWrite=p.toOpacity===1;p.mesh.visible=p.toOpacity===1}}if(t===1)animating=false}
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{mode=b.dataset.view;transition()});select.onchange=()=>{color=select.value;transition()};
const bounds=new THREE.Box3();
for(const p of parts){p.mesh.geometry.computeBoundingBox();const box=p.mesh.geometry.boundingBox;bounds.union(box);bounds.union(box.clone().translate(p.expanded));}
const center=bounds.getCenter(new THREE.Vector3()),radius=Math.max(bounds.getSize(new THREE.Vector3()).length()/2,.001);
camera.near=radius/1000;camera.far=radius*100;controls.target.copy(center);controls.minDistance=radius*.2;controls.maxDistance=radius*20;
let previousFit=0;
const resize=()=>{const r=host.getBoundingClientRect();renderer.setSize(r.width,r.height);camera.aspect=r.width/r.height;
const angle=Math.min(THREE.MathUtils.degToRad(camera.fov)/2,Math.atan(Math.tan(THREE.MathUtils.degToRad(camera.fov)/2)*camera.aspect));
const fit=radius/Math.sin(angle)*1.1;
if(!previousFit)camera.position.copy(center).add(new THREE.Vector3(1,-2.4,.8).normalize().multiplyScalar(fit));
else camera.position.sub(controls.target).multiplyScalar(fit/previousFit).add(controls.target);
previousFit=fit;camera.updateProjectionMatrix();controls.update();};new ResizeObserver(resize).observe(host);resize();updateList();

renderer.setAnimationLoop(now=>{step(now);controls.update();renderer.render(scene,camera)});
window.splitPrintViewer={getState:()=>({mode,color,animating,parts:parts.map(p=>({name:p.mesh.name,color:p.color,visible:p.mesh.visible,opacity:p.mesh.material.opacity,position:p.mesh.position.toArray()})),triangles:renderer.info.render.triangles}),ready:true};
