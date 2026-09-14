import bpy, bmesh, math, os, tempfile
from mathutils import Vector
# ===== 3D-Logo nurovelle: Kontur direkt als Mesh (robust, konkav) + runder Punkt =====
OUT=os.path.join(tempfile.gettempdir(),"logo3d_render.png")
PREVIEW=os.environ.get("PREVIEW")=="1"

# Kontur des "N" in Blender-Einheiten (aus dem Logo getract)
PN=[(0.141,-0.069),(0.117,-0.097),(0.105,-0.136),(0.108,-1.229),(0.307,-1.232),(0.315,-1.224),(0.315,-0.35),(0.323,-0.34),(0.966,-0.708),(0.989,-0.729),(0.987,-0.963),(0.977,-0.968),(0.666,-0.788),(0.657,-0.774),(0.652,-0.634),(0.447,-0.515),(0.442,-0.527),(0.442,-0.847),(0.451,-0.887),(0.465,-0.911),(0.499,-0.938),(1.053,-1.258),(1.073,-1.265),(1.114,-1.265),(1.162,-1.242),(1.189,-1.21),(1.201,-1.168),(1.201,-0.655),(1.194,-0.625),(1.179,-0.599),(1.139,-0.566),(0.24,-0.049),(0.204,-0.045),(0.172,-0.051)]
DOT=(1.0862,-0.1884,0.1486)   # Punkt: x, y, Radius

T=0.10        # Dicke (Tiefe)
BEV=0.012     # Kantenrundung vorn/hinten
TURN=22       # Drehung um senkrechte Achse (Grad): rechte Kante = Drehpunkt, linke Seite nach hinten

sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=40; sc.render.resolution_x=800; sc.render.resolution_y=800
else: sc.cycles.samples=150; sc.render.resolution_x=1500; sc.render.resolution_y=1500
sc.render.film_transparent=True; sc.cycles.max_bounces=8

if bpy.context.mode!='OBJECT':
    try: bpy.ops.object.mode_set(mode='OBJECT')
    except Exception: pass
for o in list(bpy.data.objects): bpy.data.objects.remove(o,do_unlink=True)
for c in (bpy.data.materials,bpy.data.meshes):
    for x in list(c):
        try:c.remove(x)
        except:pass

def s2l(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def mat(name,rgb,rough=0.30,metal=0.0):
    m=bpy.data.materials.new(name); m.use_nodes=True; p=m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value=(s2l(rgb[0]),s2l(rgb[1]),s2l(rgb[2]),1)
    p.inputs["Roughness"].default_value=rough; p.inputs["Metallic"].default_value=metal
    try: p.inputs["Coat Weight"].default_value=0.35
    except Exception: pass
    return m
TEAL=mat("gold",(0.85,0.60,0.18),rough=0.20,metal=1.0)      # Gold (Logo)
LIME=mat("gold_hell",(0.95,0.78,0.40),rough=0.22,metal=1.0)  # helleres Gold (Punkt)

# ---- N: Kontur -> gefuellte Flaeche (triangle_fill) -> Dicke (solidify) ----
bm=bmesh.new()
vs=[bm.verts.new((x,y,0)) for (x,y) in PN]
for i in range(len(vs)):
    bm.edges.new((vs[i],vs[(i+1)%len(vs)]))
bmesh.ops.triangle_fill(bm,use_beauty=True,use_dissolve=True,edges=bm.edges[:])
me=bpy.data.meshes.new("N"); bm.to_mesh(me); bm.free()
N=bpy.data.objects.new("N",me); sc.collection.objects.link(N)
N.data.materials.append(TEAL)
sol=N.modifiers.new("s","SOLIDIFY"); sol.thickness=T; sol.offset=0
bpy.context.view_layer.objects.active=N; bpy.ops.object.modifier_apply(modifier="s")
bev=N.modifiers.new("b","BEVEL"); bev.width=BEV; bev.segments=3; bev.limit_method='ANGLE'; bev.angle_limit=math.radians(40)
bpy.ops.object.modifier_apply(modifier="b")
bpy.ops.object.shade_smooth()
try: N.data.use_auto_smooth=True
except Exception: pass

# ---- runder Punkt ----
bpy.ops.mesh.primitive_cylinder_add(vertices=72,radius=DOT[2],depth=T,location=(DOT[0],DOT[1],0))
dot=bpy.context.object; dot.name="Punkt"
bv=dot.modifiers.new("b","BEVEL"); bv.width=BEV; bv.segments=3; bv.limit_method='ANGLE'
bpy.context.view_layer.objects.active=dot; bpy.ops.object.modifier_apply(modifier="b")
bpy.ops.object.shade_smooth(); dot.data.materials.append(LIME)

# ---- N + Punkt: zentrieren, aufstellen, skalieren ----
for o in bpy.data.objects: o.select_set(False)
N.select_set(True); dot.select_set(True); bpy.context.view_layer.objects.active=N
bpy.ops.object.join()
LOGO=bpy.context.view_layer.objects.active; LOGO.name="Logo"
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY',center='BOUNDS')
LOGO.location=(0,0,0)
LOGO.rotation_euler=(math.pi/2,0,0)          # aufstellen -> Front zur Kamera (-Y)
f=1.9/max(LOGO.dimensions.x,LOGO.dimensions.z); LOGO.scale=(f,f,f)
bpy.ops.object.transform_apply(rotation=True,scale=True)
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY',center='BOUNDS'); LOGO.location=(0,0,0)
# Drehung um senkrechte Achse (Z) am rechten Rand: rechte Kante bleibt, linke Seite nach hinten (+Y)
th=math.radians(-TURN)
hw=LOGO.dimensions.x/2.0
LOGO.rotation_euler=(0,0,th)
LOGO.location=(hw*(1-math.cos(th)), -hw*math.sin(th), 0)

# ---- Studio ----
bpy.ops.object.light_add(type='AREA',location=(3,-4,5)); k=bpy.context.object; k.data.energy=1400; k.data.size=6
bpy.ops.object.light_add(type='AREA',location=(-4,-3,3)); fl=bpy.context.object; fl.data.energy=500; fl.data.size=6
bpy.ops.object.light_add(type='AREA',location=(0,3.5,2.5)); rim=bpy.context.object; rim.data.energy=650; rim.data.size=5
wd=bpy.data.worlds['World']; wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.20,0.18,0.15,1)
wd.node_tree.nodes['Background'].inputs[1].default_value=1.3

bpy.context.view_layer.update()
ctr=sum((LOGO.matrix_world@Vector(c) for c in LOGO.bound_box),Vector())/8.0  # Bild-Mittelpunkt
cam_d=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cam_d); sc.collection.objects.link(cam)
cam.location=(ctr.x+0.45,-5.6,ctr.z+0.35); sc.camera=cam; cam_d.lens=95
cam.rotation_euler=(ctr-cam.location).to_track_quat('-Z','Y').to_euler()

try:
    sc.render.filepath=OUT; bpy.ops.render.render(write_still=True); print("RENDER_OK ->",OUT)
except Exception as e: print("Render/Save uebersprungen:",e)
