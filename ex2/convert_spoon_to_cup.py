###########################################################
# FILE : convert_spoon_to_cup.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: a simple method which convert the number of
# spoons given as parameters to cups.
#############################################################
SPOONS_IN_CUP = 3.5


def convert_spoon_to_cup(spoons):
    """
    :param spoons: float or int that represents the number of spoons needed.
    :return: int or float that represents the number of cups equivalent to
    the given amount of spoons.
    """
    cup = spoons / SPOONS_IN_CUP
    return cup

