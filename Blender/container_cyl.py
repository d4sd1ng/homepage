import bpy, bmesh, math, os, tempfile
from mathutils import Vector
OUT=os.path.join(tempfile.gettempdir(),"container_cyl_render.png")
PREVIEW=os.environ.get("PREVIEW")=="1"
sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=30; sc.render.resolution_x=640; sc.render.resolution_y=760
else: sc.cycles.samples=120; sc.render.resolution_x=1000; sc.render.resolution_y=1180
sc.render.film_transparent=False; sc.cycles.max_bounces=16
try: sc.cycles.transmission_bounces=12
except Exception: pass

# in OBJECT-Mode + Szene kontext-unabhaengig leeren
if bpy.context.mode!='OBJECT':
    try: bpy.ops.object.mode_set(mode='OBJECT')
    except Exception: pass
for o in list(bpy.data.objects): bpy.data.objects.remove(o,do_unlink=True)
for c in (bpy.data.materials,bpy.data.meshes):
    for x in list(c):
        try:c.remove(x)
        except:pass

# ---------- Materialien (wie Box: glaenzend dunkel, Gold, Glas) ----------
METAL=bpy.data.materials.new("metal"); METAL.use_nodes=True; b=METAL.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value=(0.05,0.055,0.065,1); b.inputs["Metallic"].default_value=1.0   # echtes Metall, glatt (keine Streifen)
b.inputs["Roughness"].default_value=0.28
GOLD=bpy.data.materials.new("gold"); GOLD.use_nodes=True; g=GOLD.node_tree.nodes["Principled BSDF"]
g.inputs["Base Color"].default_value=(0.85,0.60,0.18,1); g.inputs["Metallic"].default_value=1.0; g.inputs["Roughness"].default_value=0.20
GLASS=bpy.data.materials.new("glass"); GLASS.use_nodes=True; gb=GLASS.node_tree.nodes["Principled BSDF"]
gb.inputs["Base Color"].default_value=(0.86,0.89,0.93,1); gb.inputs["Roughness"].default_value=0.06
gb.inputs["Transmission Weight"].default_value=0.0      # KEINE Transmission -> keine Brechung
gb.inputs["Alpha"].default_value=0.16                   # durchsichtig ueber Alpha -> Licht wird NICHT gebrochen, keine Vase
try: GLASS.blend_method='BLEND'
except Exception: pass

def apply_bool(target,cutter,op='DIFFERENCE'):
    md=target.modifiers.new("b","BOOLEAN"); md.operation=op; md.object=cutter; md.solver='EXACT'
    bpy.context.view_layer.objects.active=target; bpy.ops.object.modifier_apply(modifier="b")
    bpy.data.objects.remove(cutter,do_unlink=True)

def cyl(name,r,z0,z1,mat,vtx=96,bevel=0.0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vtx,radius=r,depth=(z1-z0),location=(0,0,(z0+z1)/2))
    o=bpy.context.object; o.name=name
    if bevel>0:
        bv=o.modifiers.new("b","BEVEL"); bv.width=bevel; bv.segments=4; bv.limit_method='ANGLE'
        bpy.context.view_layer.objects.active=o; bpy.ops.object.modifier_apply(modifier="b")
    try: bpy.ops.object.shade_auto_smooth(angle=math.radians(40))
    except Exception:
        try: bpy.ops.object.shade_smooth(use_auto_smooth=True, auto_smooth_angle=math.radians(40))
        except Exception: bpy.ops.object.shade_smooth()
    if mat: o.data.materials.append(mat)
    return o

# ---------- Masse ----------
R=1.15          # Radius Kappen/Basis
Rg=0.98         # Radius Glas
hb=0.60         # Basis-Hoehe
hg=2.70         # Glas-Hoehe
ht=0.75         # Kappen-Hoehe
zbt=hb          # Oberkante Basis
zgt=hb+hg       # Oberkante Glas / Unterkante Kappe
H=hb+hg+ht

# ---------- Basis unten ----------
cyl("base",R,0.0,hb,METAL,bevel=0.06)
cyl("gring_b",R+0.006,hb-0.18,hb-0.05,GOLD,bevel=0.015)          # Goldring nahe Basis-Oberkante

# ---------- Glaszylinder (Rohr, hohl) ----------
gout=cyl("glass",Rg,zbt-0.02,zgt+0.02,GLASS)
inner=cyl("glass_in",Rg-0.04,zbt-0.15,zgt+0.15,None)
apply_bool(gout,inner)
glass_coll=bpy.data.collections.new("Glas"); sc.collection.children.link(glass_coll)   # Glas -> eigene Collection (ausblendbar)
for c in list(gout.users_collection): c.objects.unlink(gout)
glass_coll.objects.link(gout)

# ---------- Kappe oben ----------
cap=cyl("cap",R,zgt,H,METAL,bevel=0.06)
lidcut=cyl("lidcut",R-0.16,H-0.06,H+0.15,None)                   # eingesetzte Deckplatte (Mulde oben)
apply_bool(cap,lidcut)
cyl("gring_t",R+0.006,zgt+0.05,zgt+0.18,GOLD,bevel=0.015)        # Goldring nahe Kappen-Unterkante

# ---------- zwei kleine Punkte vorne an der Kappe ----------
for dx in (-0.20,0.20):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20,radius=0.028,depth=0.05,location=(dx,-R+0.03,H-0.22),rotation=(math.pi/2,0,0))
    d=bpy.context.object; d.data.materials.append(GOLD); bpy.ops.object.shade_smooth()   # Punkte gold

# ---------- Studio ----------
bpy.ops.mesh.primitive_plane_add(size=60,location=(0,3.2,0)); bd=bpy.context.object; bd.rotation_euler=(math.pi/2,0,0)
bd.data.materials.append(_bg:=bpy.data.materials.new("bg")); _bg.use_nodes=True
_bg.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.34,0.34,0.35,1)
_bg.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.92
bpy.ops.mesh.primitive_plane_add(size=60,location=(0,0,0)); fl=bpy.context.object
fl.data.materials.append(_fl:=bpy.data.materials.new("fl")); _fl.use_nodes=True
_fl.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.30,0.30,0.32,1)
_fl.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.5
wd=bpy.data.worlds['World']; wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.5,0.5,0.52,1)
wd.node_tree.nodes['Background'].inputs[1].default_value=1.1
bpy.ops.object.light_add(type='AREA',location=(4,-5,7)); k=bpy.context.object; k.data.energy=2600; k.data.size=7
bpy.ops.object.light_add(type='AREA',location=(-5,-2,5)); f=bpy.context.object; f.data.energy=900; f.data.size=7

cam_d=bpy.data.cameras.new('cam'); cam=bpy.data.objects.new('cam',cam_d); sc.collection.objects.link(cam)
cam.location=(4.8,-18.0,3.0); sc.camera=cam; cam_d.lens=120
cam.rotation_euler=(Vector((0,0,H*0.5))-cam.location).to_track_quat('-Z','Y').to_euler()

try:
    sc.render.filepath=OUT
    bpy.ops.render.render(write_still=True)
    print("RENDER_OK ->",OUT)
except Exception as e:
    print("Render/Save uebersprungen (Geometrie ist fertig):",e)
