import bpy, math, os, tempfile
from mathutils import Vector
OUT=os.path.join(tempfile.gettempdir(),"connection_glass_render.png")
PREVIEW=os.environ.get("PREVIEW")=="1"
sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=32; sc.render.resolution_x=900; sc.render.resolution_y=520
else: sc.cycles.samples=120; sc.render.resolution_x=1400; sc.render.resolution_y=820
sc.render.film_transparent=False; sc.cycles.max_bounces=10

if bpy.context.mode!='OBJECT':
    try: bpy.ops.object.mode_set(mode='OBJECT')
    except Exception: pass
for o in list(bpy.data.objects): bpy.data.objects.remove(o,do_unlink=True)
for c in (bpy.data.materials,bpy.data.meshes):
    for x in list(c):
        try:c.remove(x)
        except:pass

METAL=bpy.data.materials.new("metal"); METAL.use_nodes=True; b=METAL.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value=(0.05,0.055,0.065,1); b.inputs["Metallic"].default_value=1.0; b.inputs["Roughness"].default_value=0.28
GOLD=bpy.data.materials.new("gold"); GOLD.use_nodes=True; g=GOLD.node_tree.nodes["Principled BSDF"]
g.inputs["Base Color"].default_value=(0.85,0.60,0.18,1); g.inputs["Metallic"].default_value=1.0; g.inputs["Roughness"].default_value=0.20
# klares Glas ueber Alpha (keine Verzerrung), zeigt den gruenen Fluss innen
GLASS=bpy.data.materials.new("glass"); GLASS.use_nodes=True; gb=GLASS.node_tree.nodes["Principled BSDF"]
gb.inputs["Base Color"].default_value=(0.88,0.93,0.97,1); gb.inputs["Roughness"].default_value=0.03
gb.inputs["Transmission Weight"].default_value=0.0; gb.inputs["Alpha"].default_value=0.12
try: GLASS.blend_method='BLEND'
except Exception: pass
# gruen leuchtend (Strom/Partikel)
GREEN=bpy.data.materials.new("greenglow"); GREEN.use_nodes=True; gr=GREEN.node_tree.nodes["Principled BSDF"]
gr.inputs["Base Color"].default_value=(0.06,0.6,0.2,1)
gr.inputs["Emission Color"].default_value=(0.15,1.0,0.35,1); gr.inputs["Emission Strength"].default_value=6.0

def rbox(name,loc,dims,bevel,mat):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=name; o.scale=dims
    bpy.ops.object.transform_apply(scale=True)
    if bevel>0:
        bv=o.modifiers.new("b","BEVEL"); bv.width=bevel; bv.segments=4; bv.limit_method='ANGLE'
        bpy.context.view_layer.objects.active=o; bpy.ops.object.modifier_apply(modifier="b")
    bpy.ops.object.shade_smooth(); o.data.materials.append(mat); return o

def disc_x(r,x,depth,mat,vtx=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vtx,radius=r,depth=depth,location=(x,YY,ZZ),rotation=(0,math.pi/2,0))
    o=bpy.context.object; o.data.materials.append(mat); bpy.ops.object.shade_smooth(); return o

# ---- zwei Platzhalter-Container ----
BW=1.4; gap=1.7; YY=-0.15; ZZ=0.85
lx=-(BW/2+gap/2); rx=(BW/2+gap/2)
rbox("cont_l",(lx,0,0.75),(BW,1.2,1.5),0.12,METAL)
rbox("cont_r",(rx,0,0.75),(BW,1.2,1.5),0.12,METAL)

xL=lx+BW/2; xR=rx-BW/2
r_tube=0.10
# Andock-Panel je Ende: GOLDRAHMEN mit runden Ecken + dunkles Panel (wie Container)
for x,fd in ((xL,1),(xR,-1)):
    rbox("dock_gold",(x,YY,ZZ),(0.05,0.36,0.36),0.06,GOLD)          # goldener Rahmen (runde Ecken)
    rbox("dock_panel",(x+fd*0.012,YY,ZZ),(0.06,0.27,0.27),0.05,METAL)  # dunkles Panel davor -> Gold als Rand
# Glasrohr + gruener Kern zwischen den Panels
disc_x(r_tube, (xL+xR)/2, (xR-xL)-0.05, GLASS)
disc_x(0.026, (xL+xR)/2, (xR-xL)-0.10, GREEN)
# gruene Partikel im Rohr (leuchtende Kugeln, entlang der Achse verteilt)
N=9
for i in range(N):
    fx=xL+0.10+(xR-xL-0.20)*(i/(N-1))
    off=0.06*math.sin(i*1.7); offz=0.05*math.cos(i*1.3)
    rr=0.020+0.012*(i%3==0)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=rr,location=(fx,YY+off,ZZ+offz))
    p=bpy.context.object; p.data.materials.append(GREEN); bpy.ops.object.shade_smooth()

# ---- Studio ----
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,3.0,0)); bd=bpy.context.object; bd.rotation_euler=(math.pi/2,0,0)
bd.data.materials.append(_bg:=bpy.data.materials.new("bg")); _bg.use_nodes=True
_bg.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.36,0.36,0.38,1)
_bg.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.95
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,0,0)); flo=bpy.context.object
flo.data.materials.append(_fl:=bpy.data.materials.new("fl")); _fl.use_nodes=True
_fl.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.32,0.32,0.34,1)
_fl.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.5
wd=bpy.data.worlds['World']; wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.3,0.3,0.32,1); wd.node_tree.nodes['Background'].inputs[1].default_value=0.8
bpy.ops.object.light_add(type='AREA',location=(3,-4,6)); k=bpy.context.object; k.data.energy=1600; k.data.size=6
bpy.ops.object.light_add(type='AREA',location=(-4,-2,4)); f=bpy.context.object; f.data.energy=600; f.data.size=6

cam_d=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cam_d); sc.collection.objects.link(cam)
cam.location=(0.0,-7.5,2.2); sc.camera=cam; cam_d.lens=72
cam.rotation_euler=(Vector((0,0,0.85))-cam.location).to_track_quat('-Z','Y').to_euler()

try:
    sc.render.filepath=OUT; bpy.ops.render.render(write_still=True); print("RENDER_OK ->",OUT)
except Exception as e: print("Render/Save uebersprungen:",e)
