import numpy as np
from . import Car

def intersect_line_line(start1, end1, start2, end2):
    """Calculate the intersection between two lines
    
    Returns:
        Point of collision if two line collides or None if not
    """
    x1, y1 = start1
    x2, y2 = end1

    if x1>x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    x3, y3 = start2
    x4, y4 = end2

    if x3>x4:
        x3, x4 = x4, x3
        y3, y4 = y4, y3

    divider = ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    if divider==0:
        return None

    # calculate the direction of the lines
    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / divider
    uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / divider
    
    # if uA and uB are between 0-1, lines are colliding
    if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
        # optionally, draw a circle where the lines meet
        intersectionX = x1 + (uA * (x2-x1))
        intersectionY = y1 + (uA * (y2-y1))

        return np.array([intersectionX, intersectionY])
    return None
    


def intersect_line_car(start1, end1, car):
    vertices = car.vertices()
    distance = None
    intersection = None
    for i, j in [[0, 1], [1, 2], [2, 3], [3,0]]:
        inter = intersect_line_line(start1, end1, vertices[i], vertices[j])
        if inter is not None:
            d = np.linalg.norm(start1-inter)
            if distance is None or distance>d:
                distance = d
                intersection = inter
    return distance, intersection

