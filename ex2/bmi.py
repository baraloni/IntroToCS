###########################################################
# FILE : bmi.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: a simple method which calculates one's bmi based
# on height and weight values given as parameters.
# returns true if the bmi value is in the range, false otherwise.
#############################################################


def is_normal_bmi(weight, height):
    """
    :param weight: a number representing the weight
    :param height: a number representing the height
    :return: true if the bmi value is in the range, false otherwise
    """
    bmi = weight / (height**2)
    return (18.5 <= bmi) & (bmi <= 24.9)
    # if one of the conditions don't exist, means: bmi too height ot low the boolean exp. returns false,
    # if they both hold it returns true, due to the definition of '&' .


