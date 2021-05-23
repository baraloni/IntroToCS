###########################################################
# FILE : quadratic_equation.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: calculates and return or print the solutions of
# a quadratic equation which coefficients given as parameters or by user.
#############################################################
COEFFICIENT_REQUEST = "Insert coefficients a, b, and c: "
NO_SOLUTIONS = "The equation has no solutions"
ONE_SOLUTION = "The equation has 1 solution: "
TWO_SOLUTIONS = "The equation has 2 solutions: "


def discriminant_val(fst_coefficient, sec_coefficient, trd_coefficient):
    """
    quadratic equation: aX**2 + bX + c
    discriminant: b**2 - 4ac
    :param fst_coefficient: a number representing 'a' in a quadratic equation
            (int or float)
    :param sec_coefficient: a number representing 'b' in a quadratic equation
            (int or float)
    :param trd_coefficient: a number representing 'c' in a quadratic equation
            (int or float)
    :return: the value of the discriminant of the equation defined by the given coefficients
    """
    return sec_coefficient**2 - (4 * fst_coefficient * trd_coefficient)


def quadratic_equation(fst_coefficient, sec_coefficient, trd_coefficient):
    """
    the solutions of the quadratic equation: aX**2 + bX + c
    :param fst_coefficient: a number representing 'a' in a quadratic equation
            (int or float)
    :param sec_coefficient: a number representing 'b' in a quadratic equation
            (int or float)
    :param trd_coefficient: a number representing 'c' in a quadratic equation
            (int or float)
    :return: tuple (x1, x2) when x1, x2 are the equation's solutions.
    (when x1 or x2 is none: means a lack of solution).
    """
    discriminant = discriminant_val(fst_coefficient, sec_coefficient, trd_coefficient)
    if discriminant < 0:
        return None, None
    fst_sol = (-sec_coefficient - discriminant**(1/2)) / (2 * fst_coefficient)
    sec_sol = (-sec_coefficient + discriminant**(1/2)) / (2 * fst_coefficient)
    if discriminant == 0:
        if fst_sol is not None:
            return fst_sol, None
        return sec_sol, None
    return fst_sol, sec_sol


def quadratic_equation_user_input():
    """
    prints the solutions of the quadratic equation given by user input.
    """
    coefficients_str = input(COEFFICIENT_REQUEST)
    coefficients_lst = coefficients_str.split(" ")
    fst_coefficient, sec_coefficient, trd_coefficient =\
        float(coefficients_lst[0]), float(coefficients_lst[1]), float(coefficients_lst[2])
    discriminant = discriminant_val(fst_coefficient, sec_coefficient, trd_coefficient)
    if discriminant < 0:
        print(NO_SOLUTIONS)
        return
    (fst_sol, sec_sol) = quadratic_equation(fst_coefficient, sec_coefficient, trd_coefficient)
    if discriminant == 0:
        print(ONE_SOLUTION + str(fst_sol))
    else:
        print(TWO_SOLUTIONS + str(fst_sol) + ' and ' + str(sec_sol))

