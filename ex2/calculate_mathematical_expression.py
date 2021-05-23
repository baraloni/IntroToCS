###########################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: Multiply, divide, subtract or add 2 given numbers,
#  based on a given operator, as parameters or as string of the form:
#  num1, operator, num2. order matters.
#############################################################


def calculate_mathematical_expression(fst_num, sec_num, operator):
    """
    Multiply, divide, subtract or add 2 given numbers, based on a given operator.
    :param fst_num: a number (int or float)
    :param sec_num: a number (int or float)
    :param operator: an operator: /, *, -, +
    :return: the result of the operator's implementation on the given 2 numbers,
    when order matters. when given an un valid operators, or when dividing by zero
    the method will returns 'None'.
    """
    if operator == '*':
        return fst_num * sec_num
    elif operator == '/':
        if sec_num == 0:
            return None
        return fst_num / sec_num
    elif operator == "+":
        return fst_num + sec_num
    elif operator == '-':
        return fst_num - sec_num
    return None  # if 1 of the terms will happen the program won't reach this line,
    #  otherwise this line should happen. so no need for "else"(same comment for line 10)


def calculate_from_string(calculation_str):
    """
    given a string of 2 numbers and operator multiply, divide,
    subtract or add the numbers.
    :param calculation_str: String containing a number, operator, number: in that order.
    :return: the result of the operator's implementation on the given 2 numbers, all given
    in the param, when order matters. when given an un valid operators, or when dividing by zero
    the method will returns 'None'.
    """
    calculation_lst = calculation_str.split(" ")
    fst_num = float(calculation_lst[0])
    sec_num = float(calculation_lst[2])
    operator = calculation_lst[1]
    return calculate_mathematical_expression(fst_num, sec_num, operator)


