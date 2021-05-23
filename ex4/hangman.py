##############################################################################################
# FILE : ex4.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex4 2015-2016
# DESCRIPTION :
# filter_words_list():
# search within  a list or words, for the words that can be the word in
# a pattern given, while excluding the letters the user guessed in word
#  and failed.
# choose_letter():
# according to a supplied patters, checks in a list of words that matches the
# pattern for the most common letter.
# update_word_pattern():
# updates the given pattern according to a word that define the pattern, and
# a supplied letter(that can be or not be in word)/
# run_single_game():
# according to user input get hint or try to platter words in patter. the game.
# main():
# runs the game endless rounds until the user decides to stop the game.
##############################################################################################
import string
import hangman_helper


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Goes through the words list given and appends (to an empty  list, words2)
    the words that are equal in length to the pattern supplied.
    A new loop goes through the new list (words2), and through items in wrong
    guess list, and appends to a new list (words 3) all words that does not
    include letters from wrong guest list.
    finally a new loop goes through words2 and excludes all words that does
    not have identical letters ,in identical indexes as in pattern,or that
    contains the given letter somewhere else that doesn't appears in pattern.
    :param words: list of words
    :param pattern: current pattern represented by '_' as long as the word
    :param wrong_guess_lst: list of letters that does not appear in word
    :return: A list of possible match: list of words that matches the pattern
    and do not include the characters in wrong guess list, received by
    filtering the words list.

    """
    words2 = []  # empty list1
    words3 = []  # empty list2
    for word in words:
        if len(pattern) == len(word): # comparing length
            words2.append(word)
    for word2 in words2:
        for letter in wrong_guess_lst: # checks for wrong guesses in word
            if letter not in word2:
                words3.append(word2)
    for p in range(len(pattern)):
        if pattern[p].isalpha():  # it the character in pattern is letter
            for word3 in words3:
                if pattern[p] != word3[p] or \
                        pattern.count(pattern[p]) != word3.count(word3[p]):
                # the letter doesn't have the same index in both words
                #num of times the letter appears in both words is not the same
                    words3.remove(word3)
    return words3


def choose_letter(words, pattern):
    """
    Loop that goes over the letters in abc, and counts the times each letter
    appears in a list of words given. With these values i built a dictionary,
    where the key = letter in abc, value = occurrence.
    Then im using max func to find the highest value, ant it's key.
    :param words: A list of words.
    :param pattern: A given pattern.
    :return: The most common letter in list.
    """
    abc_lst = list(string.ascii_lowercase)
    for p in pattern:
        if p in abc_lst:
            abc_lst.remove(p)
            # List of letters a-z without the given letters in pattern
    words_str = ''.join(words)  # To make it possible to use count
    dct = {}
    lst = []
    for letter in abc_lst:
        occurrence = words_str.count(letter)
        dct[letter] = occurrence
        return max(dct, key=dct.get)


def update_word_pattern(word, pattern, letters):
    """
    Turns the Pattern into a list, in order to change it.
    A loop goes through the indices in Word to find a match between the item
    in indices, and Letter supplied, and changes the pattern list accordingly.
    With no match the pattern won't change.
    Then the function converts the pattern list to an unified string and
    returns the original pattern plated with the letter chosen.
    :param word: A string of lower case letters.
    :param pattern: Length of the word, represented by underscores.
    :param letters: A chosen letter.
    :return: the pattern, integrated with the chosen letter at the right place
    """
    pattern = list(pattern)
    for i in range(len(word)):
        if letters == word[i]:
            pattern[i] = letters  # Inserts i to correct place in pattern
    pattern = ''.join(pattern)
    return pattern


def run_single_game(words_list):
    """
    start:
    setting parameters that will help us in iteration.
    iteration:
    loop that runs while the pattern is empty and we didn't pass the
    number of guesses that we shouldn't pass. we ask for input:
    if the input in o place is HINT -  we will call 2 func that will supply
    us a hint.
    if the input in 1st place is a letter we can check all occurrences as
    specified in the ex4 form. the order of 'elif' lets me use simpler
    definitions.
    end:
    if the pattern is full, we win. otherwise we loos (we are past the
    iteration part), Either way we're asked if we want to start another round.
    :param words_list:a list of words
    :return: the game
    """
    word = hangman_helper.get_random_word(words_list)   # Beginning
    wrong_guess_lst = []
    error_count = 0
    pattern = '_'*len(word)
    msg = hangman_helper.DEFAULT_MSG
    while '_' in pattern and error_count < hangman_helper.MAX_ERRORS:
    # Iteration
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, ask_play= False)
        (i, j) = hangman_helper.get_input()
        if i == hangman_helper.HINT:
                a = filter_words_list(words_list,pattern,wrong_guess_lst)
                hnt = choose_letter(a ,pattern)
                msg = hangman_helper.HINT_MSG + hnt
                hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, ask_play= False)
        elif i != hangman_helper.HINT:
                if len(j) != 1 or not j.isalpha() or j.isupper():  # non valid input
                    msg = hangman_helper.NON_VALID_MSG
                elif j in wrong_guess_lst or j in pattern:  # repeated a choice
                    msg = hangman_helper.ALREADY_CHOSEN_MSG + j
                elif j in word: # input in word (easier by previous definitions)
                    pattern = update_word_pattern(word, pattern, j)
                    msg = hangman_helper.DEFAULT_MSG
                elif j not in word: #input not in word
                    wrong_guess_lst.append(j)
                    error_count += 1
                    msg = hangman_helper.DEFAULT_MSG
    if '_' not in pattern and error_count < hangman_helper.MAX_ERRORS:  # End
        # guessed the word without disqualify.
        msg = hangman_helper.WIN_MSG
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, ask_play=True)
    else: # the pattern is not full and the ran out of errors allowed
        msg = hangman_helper.LOSS_MSG + word
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, ask_play=True)


def main():
    """
    runs the game endless rounds as ling as the user decides to stop.
    :return: endless rounds in game, until user decide not to
    """
    words = hangman_helper.load_words()
    run_single_game(words)
    play = hangman_helper.get_input()
    while play == (3, True):
        words = hangman_helper.load_words()
        run_single_game(words)
        play = hangman_helper.get_input()

if __name__ == '__main__':
        hangman_helper.start_gui_and_call_main(main)
        hangman_helper.close_gui()




