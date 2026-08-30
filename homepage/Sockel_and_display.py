# NUROVELLE – Sockel + schwebendes Rechteck (Blender / Cycles)
# ------------------------------------------------------------
# Ausfuehren: blender -b -P nurovelle_sockel.py  (oder Scripting-Tab -> Run)
# WICHTIG: OUT unten auf einen Pfad auf DEINEM Rechner aendern.
#
# Stand:
#  - nur Sockel-Bodenplatte + schwebendes Rechteck (keine Wand)
#  - Rechteck-Oberkante unveraendert, Unterkante ~1/4 des Spalts nach unten verlaengert
#  - gefuellte Gold-Platte auf der Basis; Gold-Highlights nur 1-2px Kanten
#  - Amber-LEDs vorne; Bloom/Kompositor abfangsicher
# ------------------------------------------------------------
import bpy, math, os
from mathutils import Vector
OUT="/home/claude/nurovelle/sockel3d_render.png"
PREVIEW=os.environ.get("PREVIEW")=="1"
sc=bpy.context.scene
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.use_denoising=False
for vl in sc.view_layers: vl.cycles.use_denoising=False
if PREVIEW: sc.cycles.samples=32; sc.render.resolution_x=760; sc.render.resolution_y=540
else: sc.cycles.samples=120; sc.render.resolution_x=1180; sc.render.resolution_y=840
sc.render.film_transparent=False
sc.cycles.max_bounces=10

bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete()
for c in (bpy.data.materials,bpy.data.meshes):
    for x in list(c):
        try:c.remove(x)
        except:pass

def brushed():
    m=bpy.data.materials.new("metal"); m.use_nodes=True; nt=m.node_tree; b=nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(0.035,0.035,0.042,1); b.inputs["Metallic"].default_value=1.0
    b.inputs["Roughness"].default_value=0.3
    if "Anisotropic" in b.inputs: b.inputs["Anisotropic"].default_value=0.8
    wave=nt.nodes.new("ShaderNodeTexWave"); wave.wave_type='BANDS'; wave.bands_direction='X'
    wave.inputs["Scale"].default_value=1.4; wave.inputs["Detail"].default_value=8.0; wave.inputs["Distortion"].default_value=0.6
    mr=nt.nodes.new("ShaderNodeMapRange"); mr.inputs["To Min"].default_value=0.24; mr.inputs["To Max"].default_value=0.4
    nt.links.new(wave.outputs["Fac"],mr.inputs["Value"]); nt.links.new(mr.outputs["Result"],b.inputs["Roughness"])
    return m

def gold(strength=5.0):
    m=bpy.data.materials.new("gold"); m.use_nodes=True; b=m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(1.0,0.7,0.16,1); b.inputs["Metallic"].default_value=1.0; b.inputs["Roughness"].default_value=0.25
    b.inputs["Emission Color"].default_value=(1.0,0.66,0.15,1); b.inputs["Emission Strength"].default_value=strength
    return m

METAL=brushed()
GOLD=gold(1.6)
GOLDBRIGHT=gold(2.4)
GOLDPLATE=gold(0.35)

AMBER=bpy.data.materials.new("amber"); AMBER.use_nodes=True
_b=AMBER.node_tree.nodes["Principled BSDF"]
_b.inputs["Base Color"].default_value=(1,0.6,0.1,1)
_b.inputs["Emission Color"].default_value=(1,0.5,0.06,1)
_b.inputs["Emission Strength"].default_value=6

def box(name,loc,dims,bevel=0.1,seg=5,mat=None):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc)
    o=bpy.context.object
    o.name=name
    o.scale=dims
    bpy.ops.object.transform_apply(scale=True)

    if bevel>0:
        bv=o.modifiers.new("b","BEVEL")
        bv.width=bevel
        bv.segments=seg
        bv.limit_method='ANGLE'

    bpy.ops.object.shade_smooth()

    if mat:
        o.data.materials.append(mat)

    return o

def seam(name,z,w,d,th=0.03,mat=None):
    return box(
        name,
        (0,0,z),
        (w,d,th),
        bevel=0.02,
        seg=3,
        mat=mat or GOLD
    )

def rope(name,center,su,sv,axis='Z',r_corner=0.25,r_rope=0.04,mat=None,n=96):
    # gold "rope": rounded-rectangle tube
    # axis='Z' -> frame lies in XY
    # axis='Y' -> frame lies in XZ

    cx,cy,cz=center

    hw=su/2-r_corner
    hd=sv/2-r_corner

    corners=[
        (hw,hd,0.0),
        (-hw,hd,math.pi/2),
        (-hw,-hd,math.pi),
        (hw,-hd,1.5*math.pi)
    ]

    pts=[]
    per=max(4,n//4)

    for ux,uy,a0 in corners:
        for i in range(per):
            a=a0+(math.pi/2)*(i/per)

            u=ux+r_corner*math.cos(a)
            v=uy+r_corner*math.sin(a)

            if axis=='Z':
                pts.append((cx+u,cy+v,cz))
            elif axis=='Y':
                pts.append((cx+u,cy,cz+v))
            else:
                pts.append((cx,cy+u,cz+v))

    cur=bpy.data.curves.new(name,'CURVE')
    cur.dimensions='3D'

    sp=cur.splines.new('POLY')
    sp.points.add(len(pts)-1)

    for i,p in enumerate(pts):
        sp.points[i].co=(p[0],p[1],p[2],1.0)

    sp.use_cyclic_u=True

    cur.bevel_depth=r_rope
    cur.bevel_resolution=4

    ob=bpy.data.objects.new(name,cur)
    bpy.context.scene.collection.objects.link(ob)

    if mat:
        ob.data.materials.append(mat)

    return ob


# ============================================================
# SOCKEL
# ============================================================

base = box(
    "base",
    (6.4,0,0.435),
    (19.2,3.8,0.87),
    bevel=0.12,
    seg=6,
    mat=METAL
)

# Rope folgt automatisch der Grundplatte
rope(
    "bottom_glow",
    (
        base.location.x,
        base.location.y,
        base.location.z - base.dimensions.z/2 + 0.02
    ),
    base.dimensions.x + 0.15,
    base.dimensions.y + 0.15,
    'Z',
    0.28,
    0.02,
    GOLD
)


# ============================================================
# GOLDENE PLATTE AUF DEM SOCKEL
# unabhängig von base
# ============================================================

goldplate = box(
    "goldplate",
    (6.4,-0.15,0.845),
    (18.2,2.8,0.05),
    bevel=0.03,
    seg=3,
    mat=GOLDPLATE
)


# ============================================================
# FLOATING DISPLAY
# ============================================================

WALL_H=5.0
BASE_TOP=0.87

board_top = WALL_H+0.2+WALL_H*1.3
old_bottom = WALL_H+0.2

gap = old_bottom-BASE_TOP

board_bottom = old_bottom-gap/4

BOARD_H = board_top-board_bottom
BOARD_Z = (board_top+board_bottom)/2


board = box(
    "board",
    (6.4,2.4,BOARD_Z),
    (19.2,0.16,BOARD_H),
    bevel=0.06,
    seg=4,
    mat=METAL
)


# Rope folgt automatisch dem Display
rope(
    "board_frame",
    (
        board.location.x,
        board.location.y-board.dimensions.y/2-0.01,
        board.location.z
    ),
    board.dimensions.x-0.2,
    board.dimensions.z-0.2,
    'Y',
    0.28,
    0.02,
    GOLD
)
# ---- amber LEDs on front face of base ----
for x in (-1.15,-0.9,-0.65,-0.4):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05,depth=0.03,location=(x,-1.91,0.40),rotation=(math.pi/2,0,0))
    bpy.context.object.data.materials.append(AMBER); bpy.ops.object.shade_smooth()

# ---- environment ----
bpy.ops.mesh.primitive_plane_add(size=120,location=(6,7,0)); bd=bpy.context.object; bd.rotation_euler=(math.pi/2,0,0)
bd.data.materials.append(_bg:=bpy.data.materials.new("bg")); _bg.use_nodes=True
_bg.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.1,0.1,0.12,1)
_bg.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.95
bpy.ops.mesh.primitive_plane_add(size=60,location=(0,0,0)); fl=bpy.context.object
fl.data.materials.append(_fl:=bpy.data.materials.new("fl")); _fl.use_nodes=True
_fl.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.09,0.09,0.11,1)
_fl.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value=0.35
wd=bpy.data.worlds['World'];wd.use_nodes=True
wd.node_tree.nodes['Background'].inputs[0].default_value=(0.07,0.07,0.09,1)
wd.node_tree.nodes['Background'].inputs[1].default_value=0.5
bpy.ops.object.light_add(type='AREA',location=(-8,-14,16));k=bpy.context.object;k.data.energy=6000;k.data.size=20
bpy.ops.object.light_add(type='AREA',location=(18,-8,10));f=bpy.context.object;f.data.energy=2500;f.data.size=20

cam_d=bpy.data.cameras.new('cam');cam=bpy.data.objects.new('cam',cam_d);sc.collection.objects.link(cam)
cam.location=(-1.0,-44.0,9.0);sc.camera=cam;cam_d.lens=40
cam.rotation_euler=(Vector((6.4,1.0,5.6))-cam.location).to_track_quat('-Z','Y').to_euler()

try:
    sc.use_nodes = True
    tr = sc.node_tree
    if tr is not None:
        rl = tr.nodes.get('Render Layers'); cp = tr.nodes.get('Composite')
        gl = tr.nodes.new('CompositorNodeGlare'); gl.glare_type='FOG_GLOW'; gl.quality='MEDIUM'; gl.threshold=1.9; gl.size=5
        tr.links.new(rl.outputs['Image'], gl.inputs['Image']); tr.links.new(gl.outputs['Image'], cp.inputs['Image'])
except Exception as e:
    print("Bloom/Kompositor uebersprungen:", e)

sc.render.filepath=OUT
bpy.ops.render.render(write_still=True)
print("RENDER_OK")