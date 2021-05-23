###########################################################
# FILE : shapes.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: calculates and return the area of a chosen shape:
# circle, rectangular or trapezoid, based on user input.
#############################################################
import math
SHAPES_MSG = "Choose shape (1=circle, 2=rectangle, 3=trapezoid): "


def shape_area():
    """
    :return: the chosen shape's area, based on user's input
    """
    shape = input(SHAPES_MSG)
    if shape == '1':
        radius = float(input())
        return circle_area(radius)
    elif shape == '2':
        length, width = float(input()), float(input())
        return rectangular_area(length, width)
    elif shape == '3':
        fst_side, sec_side, height = float(input()), float(input()), float(input())
        return trapezoid_area(fst_side, sec_side, height)
    else:
        return None


def circle_area(radius):
    """
    :param radius: a number (float or int) representing the circle's radius
    :return: the area of the circle
    """
    return math.pi * (radius**2)


def rectangular_area(length, width):
    """
    :param length: a number (float or int) representing the rectangular's side
    :param width: a number (float or int) representing the rectangular's other side
    :return: the rectangular's area
    """
    return length * width


def trapezoid_area(fst_side, sec_side, height):
    """
    :param fst_side: a number (float or int) representing the trapezoid's side
    :param sec_side: a number (float or int) representing the trapezoid's other side
    :param height: a number (float or int) representing the rectangular's height
    :return: the trapezoid's area
    """
    return ((fst_side + sec_side)/2) * height


