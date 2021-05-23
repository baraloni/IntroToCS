###########################################################
# FILE : ex3.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex3 2016-2017
# DESCRIPTION:
# a file of methods for practicing the use of loops:
# 1) create_list():
#   Receive input from user and display it as a list.
# 2)concat_list(str_lst):
#   Edits a list to receive a single string.
# 3)average(num_list):
#   Returns the average, when given a list of numbers.
# 4)cyclic(lst1,lst2):
#   Compares 2 lists to see if they are cyclic permutation of one another.
#   (More info: https://en.wikipedia.org/wiki/Cyclic_permutation).
#   Returns True or False accordingly.
# 5)histogram(n,num_list):
#   Returns the histogram of a given list.
#   (More about Histogram: https://en.wikipedia.org/wiki/Histogram).
# 6)prime_factors(n):
#   Returns the prime factors of a natural number.
# 7)cartesian(lst1,lst2):
#   Returns all ordered pairs (a, b), from lists A and B,
#   when a was taken from A and b was taken from B.
# 8)pairs(n,num_list):
#   When given a number and a list of numbers, returns all pairs from the list
#   which sum up to be the number first received.
#  assistant methods:
# 1)find_cyclic_forms(lst, shift):
#   find the cyclic form of a given list, by shifting its items to the right, 'shift' seats.
# 2)check_if_factor(number, factor):
#   returns True if factor is number's factor, false otherwise
#############################################################
STOPPER_STRING = ""  # input that will end the create_list func's request for input


def create_list():
    """
    store user's input in a list, by entering order,
    until the user logs a string that matches the stopper string.
    :return: a list of all user input logs, by entering order.
    the stopper string will not appear at an item in the list.
    """
    input_list = []
    input_from_user = input()
    while input_from_user != STOPPER_STRING:
        input_list.append(input_from_user)
        input_from_user = input()
    return input_list


def concat_list(str_lst):
    """
    concatenate the string's in the given list, and returns the outcome.
    :param str_lst: a list of strings
    :return: a string that is the list's strings concatenation,
    or an empty string, if str_lst is an empty list.
    """
    concatenation = ''
    if len(str_lst) != 0:
        for string in str_lst:
            concatenation = concatenation + string
    return concatenation


def average(num_list):
    """
    sums all nums in the given list and returns their average in
    floating point (automatic on python 3), or None if the list is empty.
    :param num_list:
    :return: None if nums_list is empty, otherwise a float representing the
    numbers's in list average.
    """
    nums_average = None
    nums_sum = 0
    if len(num_list) != 0:
        for num in num_list:
            nums_sum = nums_sum + num
        nums_average = nums_sum / len(num_list)  # average formula
    return nums_average


def cyclic(lst1, lst2):
    """
    :param lst1: a list
    :param lst2: a list
    :return: True is the lists are 2 cyclic forms of the same list,
    False otherwise
    """
    if lst1 == lst2:   # could be reached by including 0 in the marked line's range,
        #  but this is more effective then calling a func that returns it's parameter as is
        return True
    elif len(lst1) == len(lst2):
        for shift in range(1, len(lst1)):  #
            cyclic_form = find_cyclic_forms(lst1, shift)
            if cyclic_form == lst2:
                return True
    return False


def find_cyclic_forms(lst, shift):
    """
    :param lst: a given list
    :param shift: a non negative int
    :return: a cyclic form of lst, produced by shifting the items
    'shift''s value cells to the right.
    """
    cyclic_form = [None]*len(lst)  # initiate an 'empty' list of the size required
    for index in range(0, len(lst)):
        cyclic_index = (index + shift) % len(lst)  # formula for cyclic shifting by 'shift''s val
        cyclic_form[cyclic_index] = lst[index]
    return cyclic_form


def histogram(n, num_list):
    """
    :param n: a positive int
    :param num_list: a list of non negative ints, in the range (0,n-1)
    :return: a list of size n, when the value on the i'th index stands for
    the number of times i appeared on num_list,
    """
    hist_list = [0]*n  # initiate an 'empty' list of the size required
    for index in range(len(num_list)):  # goes by the number of num_list's index
        value = num_list[index]
        hist_list[value] += 1
    return hist_list


def prime_factors(n):
    """
    :param n: a positive int >= 1
    :return:  a list of all n's prime factors, in an ascending order.
    """
    factors = []
    for num in range(2, n+1):
        while check_if_factor(n, num):
            factors.append(num)
            n = n / num  # change n to the quotient
    return factors


def check_if_factor(number, factor):
    """
    :param number: a positive int >= 1
    :param factor: a positive int in the range of (2,n)
    :return: True if factor is indeed a factor for number. False otherwise
    """
    return (number % factor) == 0  # definition of a divider


def cartesian(lst1, lst2):
    """
    :param lst1: a list of 0 or more items
    :param lst2: a list of 0 or more items
    :return: a list of all ordered pairs (tuples) of lst1 and lst2 where:
    the first item in the tuple is from list1, and the second item is from list2.
    """
    cartesian_couples = []
    if (len(lst1) != 0) or (len(lst2) != 0):
        for item_lst1 in lst1:
            for item_lst2 in lst2:
                cartesian_couples.append((item_lst1, item_lst2))
    return cartesian_couples


def pairs(n, num_list):
    """
    :param n: an int
    :param num_list: a list of ints, when every item appears only once in the list
    :return: a list of lists of size 2.
    the list contains all of the couples ( items from num_list) which adds up to n.
    """
    pairs_list = []
    checked_numbers = []
    for num in num_list:
        if num not in checked_numbers:
            checked_numbers.append(num)
            wanted_num = n - num  # calculation of num complement
            if (wanted_num in num_list) & (wanted_num not in checked_numbers):
                checked_numbers.append(wanted_num)
                pairs_list.append([num, wanted_num])
    return pairs_list







