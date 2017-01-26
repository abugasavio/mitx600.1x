import math


def polysum(n, s):
    """
    n: the number of sides of the polygon
    s: the length of each side
    returns: sum of the area and square of the perimeter of the regular polygon rounded to 4 decimal places
    """
    perimeter = n * s
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    return round(area + perimeter ** 2, 4)

