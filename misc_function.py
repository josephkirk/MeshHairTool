import pymel.core as pm
import random as rand

def mirror_transform(ob, axis="x",xform=[0,4]):
    axisDict = {
        "x":('tx', 'ry', 'rz', 'sx'),
        "y":('ty', 'rx', 'rz', 'sy'),
        "z":('tz', 'rx', 'ry', 'sz')}
    if type(ob) == pm.nt.Transform:
        for at in axisDict[axis][xform[0]:xform[1]]:
            ob.attr(at).set(ob.attr(at).get()*-1)

def random_uv_inU(ob ,offset=0.1):
    if type(ob.getShape()) == pm.nt.Mesh:
        pm.polyEditUV(ob.map, u=rand.uniform(-offset, offset))

def lock_transform(ob,lock=True):
    for at in ['translate','rotate','scale']:
        ob.attr(at).set(lock=lock)

def add_vray_OpenSubdiv_attr(ob):
    '''add Vray OpenSubdiv attr to enable smooth mesh render'''
    if str(pm.getAttr('defaultRenderGlobals.ren')) == 'vray':
        obShape = pm.listRelatives(ob, shapes=True)[0]
        pm.vray('addAttributesFromGroup', obShape, "vray_opensubdiv", 1)
        pm.setAttr(obShape+".vrayOsdPreserveMapBorders", 2)
