###########################################################
# FILE : largest_and_smallest.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: a simple method which returns the maximal and
# minimal number out of the 3 numbers given as a tuple:
# the number on left is the largest and the right one is the smallest.
#############################################################

def largest_and_smallest(fst_num, sec_num, trd_num):
    """
    :param fst_num: a number (int or float)
    :param sec_num: a number (int or float)
    :param trd_num: a number (int or float)
    :return: the largest and smallest of the 3 given numbers,
    when the number on left is the largest and the right one is the smallest
    """
    if fst_num > sec_num:
        if fst_num > trd_num:
            if sec_num > trd_num:
                return fst_num, trd_num
            return fst_num, sec_num
        return trd_num, sec_num
    else:
        if fst_num < trd_num:
            if sec_num < trd_num:
                return trd_num, fst_num
            return sec_num, fst_num
        return sec_num, trd_num

