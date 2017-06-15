import pymel.core as pm


class HairObj(object):
    """hair Mesh object"""
    def __init__(self, name, lengthDivisions, widthDivisions, ctrls):
        self.name = name
        self.lengthdivs = lengthDivisions
        self.widthdivs = widthDivisions
        self.ctrls = ctrls

    def create(self):
        """generate hairMesh"""
        pass


class HairCtrlObj(object):
    """ctrl for hairobj"""
    common_color = (0.2, 0.5, 0.2)
    ###############################################
    def __init__(self, name, shapeType, radius, color):
        self.name = name
        self.shapetype = shapeType
        self.radius = radius
        self.color = color
        self.create()

    def color_change(self):
        """update change in color"""
        for atr in [('overrideEnabled', 1),
                    ('overrideRGBColors', 1),
                    ('overrideColorRGB', self.color)]:
            self.shape_node.attr(atr[0]).set(atr[1])

    def get_shape_info(self, pos):
        """return appropriate data for ctrl generation"""
        shape_type = {
            'circle':(3, 8),
            'triangle':(1, 3),
            'diamond':(1, 4)
        }
        return shape_type[self.shapetype][pos]

    def create(self):
        """"generate Control Shape"""
        temp_ob = pm.circle(c=(0, 0, 0),
                            nr=(0, 1, 0),
                            sw=360, r=self.radius,
                            name=self.name,
                            d=self.get_shape_info(0),
                            s=self.get_shape_info(1),
                            ut=0, tol=5.77201e-008, ch=1)
        self.transform = temp_ob[0]
        self.shape_node = self.transform.getShape()
        self.gen_node = temp_ob[1]

    @classmethod
    def circle(cls, name='CircleControl#', radius=1.0, color=common_color):
        """Create circle controls"""
        return HairCtrlObj(name, 'circle', radius, color)

    @classmethod
    def triangle(cls, name='TriangleControl#', radius=1.0, color=common_color):
        """Create triangle controls"""
        return HairCtrlObj(name, 'triangle', radius, color)

    @classmethod
    def diamond(cls, name='DiamondControl#', radius=1.0, color=common_color):
        """Create diamond controls"""
        return HairCtrlObj(name, 'diamond', radius, color)
