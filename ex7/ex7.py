################################################################################
# FILE : ex7.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex7 2016-2017
# DESCRIPTION :
# a set of recursive methods. created in order to practice a recursive
# way of solution. more info on the methods documentation and README
################################################################################


def print_to_n(n):
    """
    prints all natural numbers in ascending order, from 1 to n.
    :param n: int.
    :return: prints all natural numbers, ascending, from 1 to n.
    """
    if n < 1:
        return
    print_to_n(n-1)
    print(n)


def print_reversed(n):
    """
    prints all natural numbers in descending order, from n to 1.
    :param n: int.
    :return: prints all natural numbers, from n, descending to 1.
    """
    if n < 1:
        return
    print(n)
    print_reversed(n-1)


def is_prime(n):
    """
    Determines whether an inserted number(int) is prime.
    :param n: int.
    :return: True- in n is prime, False if it isn't.
    """
    if n <= 1:
        return False
    return has_divisor_smaller_than(n, n-1)


def has_divisor_smaller_than(n, i):
    """
    checks if n is prime.
    :param n: int > 1
    :param i: int, smaller then n
    :return: False if n has a divisor smaller or equal to i,True is doesn't.
    """
    if i == 1:
        return True
    elif n % i == 0:
        return False
    return has_divisor_smaller_than(n, i-1)


def divisors(n):
    """
    creates a list of all dividers (between n to 1, including) of n,
    from smaller to bigger.
    :param n: an int>0.
    :return: a list of all dividers (between n to 1, including) of n,
    from smaller to bigger.
    """
    lst = []
    divisors_helper(n, abs(n), lst)
    return lst


def divisors_helper(n, i, lst):
    """
    divides n in all numbers from n to i (include), and append all complete
    dividers to the list, ever changing it.
    :param n: int>0.
    :param i: int, n=i<=1
    :param lst:  a list.
    :return:a list of all dividers (between n to 1, including) of n,
    from smaller to bigger.
    """
    if i < 1:
        return
    divisors_helper(n, i-1, lst)
    if n % i == 0:
        lst.append(i)


def factorial(n):
    """
    Calculates the value of the product of all ints starting from 1 to n. (factorial).
    :param n: un-negative int.
    :return: an int, the factorial of n.
    """
    if n == 1:
        return 1
    return n * factorial(n-1)


def exp_n_x(n, x):
    """
    calculates the exponential sum function of inserted values:
    :param n: the range: int, n >= o
    :param x: the variable, a real number.
    :return: the exponential sum for the given n and x: a float.
    """
    if n == 0:
        return 1
    return ((x**n)/factorial(n)) + exp_n_x(n-1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    Solves Hanoi game.
    :param hanoi: object, graphic representation of the game.
    :param n: int. num of hoops.
    :param src: object, the source pool.
    :param dest:object, the destination pool.
    :param temp: object, the third pool.
    :return: the game solved.
    """
    if n <= 0:
        return
    elif n == 1:
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n-1, src, temp, dest)
        play_hanoi(hanoi, 1, src, dest, temp)
        play_hanoi(hanoi, n-1, temp, dest, src)


def print_binary_sequences_with_prefix(prefix, n):
    """
    prints all sequences in length n of '0','1', when given a string to work on.
    :param prefix: an empty string.
    :param n: un-negative int.
    :return: prints all sequences in length n of '0','1'.
    """
    if len(prefix) == n:
        print(prefix)
        return
    print_binary_sequences_with_prefix(prefix + '0', n)
    print_binary_sequences_with_prefix(prefix + '1', n)


def print_binary_sequences(n):
    """
    prints all sequences in length n of '0','1'.
    :param n: un-negative int.
    :return: prints all sequences in length n of '0','1'.
    """
    print_binary_sequences_with_prefix('', n)


def print_seq_helper(char_list, n, seq):
    """
    prints all combination of a seq with n characters, from the
    characters from char_lst
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :param seq: an empty string.
    :return: prints all combination of a seq with n characters, from the
    characters from char_lst.(strings)
    """
    if len(seq) == n:
        print(seq)
        return
    for char in char_list:
        print_seq_helper(char_list, n, seq+char)


def print_sequences(char_list, n):
    """
    prints all combination of a seq with n characters, from the
    characters from char_lst.
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :return: prints all combination of a seq with n characters, from the
    characters from char_lst.(strings)
    """
    print_seq_helper(char_list, n, '')


def no_rep_seq_helper(char_list, n, seq):
    """
    prints all combination of n characters, using the characters from
    char_list, when every character in seq appears exactly once.
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :param seq: an empty string.
    :return:prints all combination of n characters, using the characters from
    char_list, when every character in seq appears exactly once.(string)
    """
    if len(seq) == n:
        print(seq)
        return
    for char in char_list:
        if char not in seq:
            no_rep_seq_helper(char_list, n, seq + char)


def print_no_repetition_sequences(char_list, n):
    """
    prints all combination of n characters, using the characters from
    char_list, when every character appears no more then once.
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :return:prints all combination of n characters, using the characters from
    char_list, when every character appears no more then once.(string)
    """
    no_rep_seq_helper(char_list, n, '')


def no_rep_seq_lst_helper(char_list, n, seq, lst):
    """
    creates a list that contains all combination of n characters,
    using the characters from char_list, when every character appears
    no more then once.
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :param seq: an empty string.
    :param lst: an empty list.
    :return: returns the list it created, a list that contains all
    combination of n characters, using the characters from char_list,
    when every character appears no more then once.
    """
    if len(seq) == n:
        lst.append(seq)
        return
    for char in char_list:
        if char not in seq:
            no_rep_seq_lst_helper(char_list, n, seq + char, lst)


def no_repetition_sequences_list(char_list, n):
    """
    prints a list that contains all combination of n characters,
    using the characters from char_list, when every character appears
    no more then once.
    :param char_list: un empty list of characters.
    :param n: un negative int.
    :return: prints the list mentioned above.
    """
    lst = []
    no_rep_seq_lst_helper(char_list, n, '', lst)
    return lst


