import numpy as np
from . import Car

def intersect_line_line(start1, end1, start2, end2):
    """Calculate the intersection between two lines
    
    Returns:
        Point of collision if two line collides or None if not
    """
    x1 = start1[0]
    y1 = start1[0]
    x2 = end1[0]
    y2 = end1[0]

    x3 = start2[0]
    y3 = start2[0]
    x4 = end2[0]
    y4 = end2[0]

    # calculate the direction of the lines
    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))

    # if uA and uB are between 0-1, lines are colliding
    if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
        # optionally, draw a circle where the lines meet
        intersectionX = x1 + (uA * (x2-x1))
        intersectionY = y1 + (uA * (y2-y1))

        return np.array([intersectionX, intersectionY])
    return None
    

def intersect_line_car(start1, end1, car):
    r = car.rectangle()
