from manim import *
import math

def garc(self, point1, point2, d):
    """
    General Arc
    Draws an arc between two points where d is the distance from the circle's center to the chord
    """

    def flip_vector(point):
        flip = point.copy()
        flip[0] = point[1]
        flip[1] = -point[0]
        return flip

    sign = math.copysign(1, d)
    c = math.dist(point1, point2)
    r = math.hypot(c/2, d)
    theta = 2 * math.asin((c / 2) / r) * sign

    center = (point2 - point1) / 2
    norm = math.dist(center, [0,0,0])
    center = point1 + center + flip_vector(center) / norm * d

    sangle = math.atan2(point1[1] - center[1], point1[0] - center[0])

    return Arc(radius=r, start_angle=sangle, angle=-theta).shift(center)