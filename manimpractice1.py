
from manimlib.imports import *
import numpy as np
import math

class Shapes(GraphScene):
    CONFIG = {
        'x_min': -1,
        'x_max': 1,
        'y_min': -1,
        'y_max': 1,
        'x_tick_frequency': 2,
        'y_tick_frequency': 2,
        'graph_origin': ORIGIN,
        'x_axis_width': 5,
        'y_axis_height': 5,
        'x_axis_label': '$X$',
        'y_axis_label': '$Y$',
    }

    def construct(self):
        circle = Circle(radius = 2)
        triangle = Triangle()
        square = Square(side_length = math.sqrt(8), fill_opacity = 0.4)
        formula = TextMobject('$2 * radius ^ 2$').shift(5 * RIGHT + 3 * UP)
        eqn = TextMobject('Area of square').shift(3 * LEFT + 3 * UP)
        END = (- math.sqrt(8)/2, -math.sqrt(8)/2, 0)
        START = (math.sqrt(8)/2, math.sqrt(8)/2, 0)
        diameter = Line(START, END)       
        self.setup_axes(animate = True)
        self.play(ShowCreation(eqn),ShowCreation(diameter),  ShowCreation(formula), ShowCreation(circle))

        self.play(ShowCreation(square))
    
        self.wait(2)
