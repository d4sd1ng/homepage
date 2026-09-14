import bpy, math, os, tempfile
from mathutils import Vector
OUT=os.path.join(tempfile.gettempdir(),"connection_render.png")
PREVIEW=os.environ.get("PREVIEW")=="1"
sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=30; sc.render.resolution_x=820; sc.render.resolution_y=520
else: sc.cycles.samples=110; sc.render.resolution_x=1300; sc.render.resolution_y=820
sc.render.film_transparent=False; sc.cycles.max_bounces=8

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
# leuchtendes Gold fuer den "Strom"/Fluss
GLOW=bpy.data.materials.new("goldglow"); GLOW.use_nodes=True; gg=GLOW.node_tree.nodes["Principled BSDF"]
gg.inputs["Base Color"].default_value=(1.0,0.72,0.25,1); gg.inputs["Metallic"].default_value=1.0; gg.inputs["Roughness"].default_value=0.25
gg.inputs["Emission Color"].default_value=(1.0,0.7,0.25,1); gg.inputs["Emission Strength"].default_value=3.0

def rbox(name,loc,dims,bevel,mat):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=name; o.scale=dims
    bpy.ops.object.transform_apply(scale=True)
    if bevel>0:
        bv=o.modifiers.new("b","BEVEL"); bv.width=bevel; bv.segments=4; bv.limit_method='ANGLE'
        bpy.context.view_layer.objects.active=o; bpy.ops.object.modifier_apply(modifier="b")
    bpy.ops.object.shade_smooth(); o.data.materials.append(mat); return o

# ---- zwei Platzhalter-Container ----
BW=1.4; gap=1.4
lx=-(BW/2+gap/2); rx=(BW/2+gap/2)
rbox("cont_l",(lx,0,0.75),(BW,1.2,1.5),0.12,METAL)
rbox("cont_r",(rx,0,0.75),(BW,1.2,1.5),0.12,METAL)

# ---- Verbindung Container->Container: leuchtender Gold-Strom ----
zc=0.85
x0=lx+BW/2; x1=rx-BW/2                      # von rechter Flanke links bis linke Flanke rechts
# Hauptstrom (Rohr)
bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=0.06,depth=(x1-x0),location=((x0+x1)/2,-0.15,zc),rotation=(0,math.pi/2,0))
c=bpy.context.object; c.data.materials.append(GLOW); bpy.ops.object.shade_smooth()
# zwei duennere Begleit-Straenge (Kabel-Buendel)
for dz in (0.12,-0.12):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20,radius=0.025,depth=(x1-x0),location=((x0+x1)/2,-0.15,zc+dz),rotation=(0,math.pi/2,0))
    s=bpy.context.object; s.data.materials.append(GOLD); bpy.ops.object.shade_smooth()
# Anschlussknoten an beiden Containern
for x in (x0,x1):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12,location=(x,-0.15,zc)); n=bpy.context.object
    n.data.materials.append(GOLD); bpy.ops.object.shade_smooth()

# ---- Studio ----
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,3.0,0)); bd=bpy.context.object; bd.rotation_euler=(math.pi/2,0,0)
bd.data.materials.append(_bg:=bpy.data.materials.new("bg")); _bg.use_nodes=True
_bg.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.34,0.34,0.36,1)
_bg.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.95
bpy.ops.mesh.primitive_plane_add(size=40,location=(0,0,0)); fl=bpy.context.object
fl.data.materials.append(_fl:=bpy.data.materials.new("fl")); _fl.use_nodes=True
_fl.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.3,0.3,0.32,1)
_fl.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.5
wd=bpy.data.worlds['World']; wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.28,0.28,0.3,1)
wd.node_tree.nodes['Background'].inputs[1].default_value=0.7
bpy.ops.object.light_add(type='AREA',location=(3,-4,6)); k=bpy.context.object; k.data.energy=1600; k.data.size=6
bpy.ops.object.light_add(type='AREA',location=(-4,-2,4)); f=bpy.context.object; f.data.energy=600; f.data.size=6

cam_d=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cam_d); sc.collection.objects.link(cam)
cam.location=(0.0,-7.5,2.3); sc.camera=cam; cam_d.lens=70
cam.rotation_euler=(Vector((0,0,0.85))-cam.location).to_track_quat('-Z','Y').to_euler()

try:
    sc.render.filepath=OUT; bpy.ops.render.render(write_still=True); print("RENDER_OK ->",OUT)
except Exception as e: print("Render/Save uebersprungen:",e)
