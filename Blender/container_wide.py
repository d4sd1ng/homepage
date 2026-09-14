import bpy, bmesh, math, os, tempfile
from mathutils import Vector
OUT=os.path.join(tempfile.gettempdir(),"container_wide_render.png")   # schreibt in temp -> funktioniert ueberall
PREVIEW=os.environ.get("PREVIEW")=="1"
sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=26; sc.render.resolution_x=640; sc.render.resolution_y=700
else: sc.cycles.samples=110; sc.render.resolution_x=1000; sc.render.resolution_y=1100
sc.render.film_transparent=False; sc.cycles.max_bounces=6

# erst in OBJECT-Mode (sonst schlagen die Operatoren fehl), dann Szene kontext-unabhaengig leeren
if bpy.context.mode!='OBJECT':
    try: bpy.ops.object.mode_set(mode='OBJECT')
    except Exception: pass
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o,do_unlink=True)
for c in (bpy.data.materials,bpy.data.meshes):
    for x in list(c):
        try:c.remove(x)
        except:pass

# Koerper: Gunmetal (echtes Metall, glatt)
clay=bpy.data.materials.new("clay"); clay.use_nodes=True; b=clay.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value=(0.05,0.055,0.065,1); b.inputs["Metallic"].default_value=1.0; b.inputs["Roughness"].default_value=0.28
# Gold glaenzend
GOLD=bpy.data.materials.new("gold"); GOLD.use_nodes=True; g=GOLD.node_tree.nodes["Principled BSDF"]
g.inputs["Base Color"].default_value=(0.85,0.60,0.18,1); g.inputs["Metallic"].default_value=1.0; g.inputs["Roughness"].default_value=0.20
GOLDL=bpy.data.materials.new("goldline"); GOLDL.use_nodes=True; g2=GOLDL.node_tree.nodes["Principled BSDF"]
g2.inputs["Base Color"].default_value=(0.95,0.72,0.28,1); g2.inputs["Metallic"].default_value=1.0; g2.inputs["Roughness"].default_value=0.14
# Glas: dunkel & reflektierend
glassmat=bpy.data.materials.new("glass"); glassmat.use_nodes=True; gb=glassmat.node_tree.nodes["Principled BSDF"]
gb.inputs["Base Color"].default_value=(0.01,0.01,0.014,1); gb.inputs["Roughness"].default_value=0.03
gb.inputs["Transmission Weight"].default_value=0.85; gb.inputs["IOR"].default_value=1.45

W,D,H=4.8,1.9,2.15   # doppelt so breit (W 2.4 -> 4.8); Tiefe/Hoehe unveraendert
R_big=0.34

# ---------- solid body: only 2 front vertical edges rounded ----------
bm=bmesh.new(); bmesh.ops.create_cube(bm,size=1.0)
for v in bm.verts: v.co.x*=W; v.co.y*=D; v.co.z*=H
bm.edges.ensure_lookup_table()
frontv=[e for e in bm.edges if all(v.co.y<0 for v in e.verts) and abs(e.verts[0].co.z-e.verts[1].co.z)>0.5]
bmesh.ops.bevel(bm,geom=frontv,offset=R_big,segments=12,affect='EDGES',profile=0.5)
me=bpy.data.meshes.new("body"); bm.to_mesh(me); bm.free()
body=bpy.data.objects.new("body",me); sc.collection.objects.link(body)
body.location=(0,0,H/2); bpy.context.view_layer.objects.active=body; body.select_set(True)
bpy.ops.object.transform_apply(location=True); body.data.materials.append(clay)

def apply_bool(target,cutter,op='DIFFERENCE'):
    md=target.modifiers.new("b","BOOLEAN"); md.operation=op; md.object=cutter; md.solver='EXACT'
    bpy.context.view_layer.objects.active=target; bpy.ops.object.modifier_apply(modifier="b")
    bpy.data.objects.remove(cutter,do_unlink=True)

# ---------- HOHLSCHALE (laut Draufsicht-Schnitt): Innenraum + Fensterdurchbruch in der Vorderwand ----------
t=0.18; yf=-D/2                              # t = Wandstaerke rundum (leicht aenderbar)
# 1) Innenraum aushoehlen: allseitig um t eingerueckte Kavitaet (inkl. Vorder- und Rueckwand)
ix=W/2-t; iyf=yf+t; iyb=D/2-t; iz0=t; iz1=H-t
cav=bmesh.new(); bmesh.ops.create_cube(cav,size=1.0)
for v in cav.verts: v.co.x*=(2*ix); v.co.y*=(iyb-iyf); v.co.z*=(iz1-iz0)
mec=bpy.data.meshes.new("cav"); cav.to_mesh(mec); cav.free()
cavo=bpy.data.objects.new("cav",mec); sc.collection.objects.link(cavo)
cavo.location=(0,(iyf+iyb)/2,(iz0+iz1)/2); bpy.context.view_layer.objects.active=cavo
bpy.ops.object.transform_apply(location=True); apply_bool(body,cavo)
# 2) quadratischer Fensterdurchbruch in der Vorderwand, RUNDE Ecken
win_w,win_h=2.80,1.40; wz=1.03; corner_r=0.10   # Fenster proportional breiter (win_w verdoppelt)
cbw=bmesh.new(); bmesh.ops.create_cube(cbw,size=1.0)
for v in cbw.verts: v.co.x*=win_w; v.co.y*=(t+0.5); v.co.z*=win_h
cbw.edges.ensure_lookup_table()
yed=[e for e in cbw.edges if abs(e.verts[0].co.y-e.verts[1].co.y)>0.2]   # 4 Fenster-Eckkanten
bmesh.ops.bevel(cbw,geom=yed,offset=corner_r,segments=6,affect='EDGES',profile=0.5)
mew=bpy.data.meshes.new("win"); cbw.to_mesh(mew); cbw.free()
wino=bpy.data.objects.new("win",mew); sc.collection.objects.link(wino)
wino.location=(0, yf+(t+0.5)/2-0.25, wz); bpy.context.view_layer.objects.active=wino
bpy.ops.object.transform_apply(location=True); apply_bool(body,wino)
# ---------- GOLDENE FASE rund ums Fenster (integriert: Keil aus Koerper + goldener Keil buendig) ----------
fase=0.06   # <-- Breite der goldenen Fase (0 = keine)
def rrect(hwx,hhz,r,y,per=10):
    C=[(hwx-r,wz+hhz-r,0.0),(-(hwx-r),wz+hhz-r,0.5*math.pi),(-(hwx-r),wz-hhz+r,math.pi),(hwx-r,wz-hhz+r,1.5*math.pi)]
    pts=[]
    for cx,cz,a0 in C:
        for i in range(per+1): a=a0+(0.5*math.pi)*(i/per); pts.append((cx+r*math.cos(a),y,cz+r*math.sin(a)))
    return pts
def wedge_ring(name,fv):                       # dreieckiger Ring-Querschnitt (L1 vorne-aussen, L2 vorne-innen, L3 innen-tief)
    L1=rrect(win_w/2+fv, win_h/2+fv, corner_r+fv, yf)
    L2=rrect(win_w/2,     win_h/2,    corner_r,    yf)
    L3=rrect(win_w/2,     win_h/2,    corner_r,    yf+fv)
    n=len(L1); V=L1+L2+L3; A=0; B=n; Cc=2*n; f=[]
    for i in range(n):
        j=(i+1)%n
        f.append((A+i,A+j,Cc+j,Cc+i))          # Fasenflaeche (aussen->tief)
        f.append((A+i,B+i,B+j,A+j))            # Vorderflaeche
        f.append((B+i,Cc+i,Cc+j,B+j))          # Innenwand
    m=bpy.data.meshes.new(name); m.from_pydata(V,[],f); m.update()
    mb=bmesh.new(); mb.from_mesh(m); bmesh.ops.recalc_face_normals(mb,faces=mb.faces); mb.to_mesh(m); mb.free()
    return m
if fase>0:
    cutm=wedge_ring("fasecut",fase); co=bpy.data.objects.new("fasecut",cutm); sc.collection.objects.link(co)
    bpy.context.view_layer.objects.active=co; apply_bool(body,co)        # Keil aus Koerper entfernen
    goldm=wedge_ring("goldfase",fase); go=bpy.data.objects.new("goldfase",goldm); sc.collection.objects.link(go)
    go.location=(0,-0.0012,0)                                            # Hauch nach vorn -> kein Z-Fighting
    go.data.materials.append(GOLD)
    bpy.context.view_layer.objects.active=go; go.select_set(True); bpy.ops.object.shade_smooth()

# ---------- outline: ONLY front corners rounded, back corners sharp (matches body) ----------
def outline(z,expand=0.0,per=12):
    hw=W/2+expand; hd=D/2+expand; r=R_big
    pts=[(hw,hd,z),(-hw,hd,z)]                       # back-right, back-left (sharp)
    cx,cy=-hw+r,-hd+r
    for i in range(per+1): a=math.pi+(math.pi/2)*(i/per); pts.append((cx+r*math.cos(a),cy+r*math.sin(a),z))
    cx,cy=hw-r,-hd+r
    for i in range(per+1): a=1.5*math.pi+(math.pi/2)*(i/per); pts.append((cx+r*math.cos(a),cy+r*math.sin(a),z))
    return pts

# Nut: kurzes Stueck vorne (front_ext) -> ueber die Frontrundung -> Seiten -> Rueckseite (komplett bis hinten)
front_ext=0.05   # <-- Laenge der Nut auf der VORDERSEITE (kleiner = vorne kuerzer)
def groove_cutter(z,rtube,fe,per=10):
    hw=W/2; hd=D/2; r=R_big
    pts=[(-(hw-r)+fe,-hd,z)]                                  # vorne-links, kurzes Stueck
    cx,cy=-(hw-r),-(hd-r)
    for i in range(per+1): a=1.5*math.pi-(math.pi/2)*(i/per); pts.append((cx+r*math.cos(a),cy+r*math.sin(a),z))
    pts.append((-hw,hd,z)); pts.append((hw,hd,z))            # linke Seite -> Rueckseite -> rechte Seite
    cx,cy=(hw-r),-(hd-r)
    for i in range(per+1): a=-(math.pi/2)*(i/per); pts.append((cx+r*math.cos(a),cy+r*math.sin(a),z))
    pts.append(((hw-r)-fe,-hd,z))                            # vorne-rechts, kurzes Stueck
    cur=bpy.data.curves.new("g",'CURVE'); cur.dimensions='3D'
    sp=cur.splines.new('POLY'); sp.points.add(len(pts)-1)
    for i,p in enumerate(pts): sp.points[i].co=(p[0],p[1],p[2],1.0)
    sp.use_cyclic_u=False; cur.bevel_depth=rtube; cur.bevel_resolution=3; cur.use_fill_caps=True
    ob=bpy.data.objects.new("g",cur); sc.collection.objects.link(ob)
    bpy.context.view_layer.objects.active=ob; ob.select_set(True); bpy.ops.object.convert(target='MESH')
    return bpy.context.object

for gz in (0.55, 1.51):
    apply_bool(body, groove_cutter(gz,0.010,front_ext))   # duenner & flacher

# ---------- eingesetzte Deckplatte oben: flache Mulde in der Oberseite (laut Referenz) ----------
tp_ix=W/2-0.20; tp_iy=D/2-0.20; tp_depth=0.03
tpc=bmesh.new(); bmesh.ops.create_cube(tpc,size=1.0)
for v in tpc.verts: v.co.x*=(2*tp_ix); v.co.y*=(2*tp_iy); v.co.z*=(tp_depth*2)
mtp=bpy.data.meshes.new("toppanel"); tpc.to_mesh(mtp); tpc.free()
tpo=bpy.data.objects.new("toppanel",mtp); sc.collection.objects.link(tpo)
tpo.location=(0,0,H); bpy.context.view_layer.objects.active=tpo
bpy.ops.object.transform_apply(location=True); apply_bool(body,tpo)

try: bpy.ops.object.shade_auto_smooth(angle=math.radians(30))
except Exception:
    try: bpy.ops.object.shade_smooth(use_auto_smooth=True, auto_smooth_angle=math.radians(30))
    except Exception: bpy.ops.object.shade_flat()

# ---------- gold blende near top (wraps) + thin shining line at its lower edge ----------
def band(name,z0,z1,expand,mat):
    lo=outline(z0,expand); hi=outline(z1,expand); verts=lo+hi; n=len(lo); faces=[]
    for i in range(n):
        j=(i+1)%n; faces.append((i,j,n+j,n+i))
    m=bpy.data.meshes.new(name); m.from_pydata(verts,[],faces); m.update()
    o=bpy.data.objects.new(name,m); sc.collection.objects.link(o)
    o.data.materials.append(mat); return o
band("blende",1.96,2.12,0.004,GOLD)           # ganz oben: nur ~0.03 Material darueber (bis 2.15)
band("blende_line",1.952,1.964,0.005,GOLDL)   # Glanzlinie fast buendig (steht kaum vor)

# ---------- Glas im Fenster (eigene Collection "Glas", sichtbar; per Auge ausblendbar) ----------
glass_coll=bpy.data.collections.new("Glas"); sc.collection.children.link(glass_coll)
gm=bpy.data.meshes.new("glas"); gbm=bmesh.new(); bmesh.ops.create_cube(gbm,size=1.0)
for v in gbm.verts: v.co.x*=(win_w-0.04); v.co.y*=0.02; v.co.z*=(win_h-0.04)
gbm.to_mesh(gm); gbm.free()
glass=bpy.data.objects.new("glas",gm); glass_coll.objects.link(glass)
glass.location=(0,yf+0.04,wz); glass.data.materials.append(glassmat)
glass.hide_viewport=True; glass.hide_render=True   # Fenster offen -> Glas standardmaessig ausgeblendet

# ---------- neutral studio (kein Bloom!) ----------
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,2.6,0)); bd=bpy.context.object; bd.rotation_euler=(math.pi/2,0,0)
bd.data.materials.append(_bg:=bpy.data.materials.new("bg")); _bg.use_nodes=True
_bg.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.4,0.4,0.42,1)
_bg.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.95
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,0,0)); fl=bpy.context.object
fl.data.materials.append(_fl:=bpy.data.materials.new("fl")); _fl.use_nodes=True
_fl.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.36,0.36,0.38,1)
_fl.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.7
wd=bpy.data.worlds['World']; wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.3,0.3,0.32,1)
wd.node_tree.nodes['Background'].inputs[1].default_value=0.7
bpy.ops.object.light_add(type='AREA',location=(3,-4.5,6)); k=bpy.context.object; k.data.energy=1800; k.data.size=6
bpy.ops.object.light_add(type='AREA',location=(-4.5,-2,4)); f=bpy.context.object; f.data.energy=700; f.data.size=6

cam_d=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cam_d); sc.collection.objects.link(cam)
cam.location=(3.5,-15.5,3.0); sc.camera=cam; cam_d.lens=105   # weiter weg fuer die breite Variante
cam.rotation_euler=(Vector((0,0,1.02))-cam.location).to_track_quat('-Z','Y').to_euler()

# Render optional: scheitert das Speichern, bleibt die fertige Geometrie trotzdem erhalten
try:
    sc.render.filepath=OUT
    bpy.ops.render.render(write_still=True)
    print("RENDER_OK ->",OUT)
except Exception as e:
    print("Render/Save uebersprungen (Geometrie ist fertig):",e)
