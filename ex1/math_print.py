###########################################################
# FILE : math_print.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION:  a file that contains math methods for
# the purpose of exercising the Math module,
#############################################################
import math


def golden_ratio():
    """ this function calculates and prints the value of the golden ratio """
    golden_ratio_formula = 2 * (math.cos(math.pi/5))
    print(golden_ratio_formula)


def square_five():
    """ this function calculates and prints the value of squared five"""
    print(5**2)


def hypotenuse():
    """calculates and prints  the length of a right triangle's
     hypotenuse, whose legs are of length 5 and 4"""
    squared_hypo = (4**2) + (5**2)
    print(math.sqrt(squared_hypo))  # the root of squared hypotenuse is the hypo's length


def pi():
    """prints the value of pi"""
    print(math.pi)


def e():
    """prints the value of e"""
    print(math.e)


def squares_area():
    """ calculate and prints the area of 10 squares: whose sides
     lengths are from 1 to 10, in an ascending order """
    print(1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2)

