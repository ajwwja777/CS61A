"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    count = -1
    for p in paragraphs:
        if select(p):
            count += 1
            if count == k:
                return p
    return ''
    # END PROBLEM 1

import re
def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(p):
        for t in topic:
            if t in re.sub(r'[;()<>$.,?!\'\"*`#-+/,:]', '', p).lower().split():
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if typed_words == []:
        return 0.0
    
    correct = 0.0
    for t, r in zip(typed_words, reference_words):
        correct += (t == r)
    return 100 * correct/len(typed_words)
    """MY OLD
    accuracy = 0.0
    if typed_words == []:
        return 0.0
    word_value = 100/len(typed_words)
    for i in range(len(reference_words)):
        if typed_words[i] == reference_words[i]:
            accuracy += word_value
    return accuracy
    """
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return 60/elapsed * len(typed)/5
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    diff_nums = [diff_function(user_word, valid_word, limit) for valid_word in valid_words]
    min_num = min(diff_nums)
    min_index = diff_nums.index(min_num)
    if min_num > limit:
        return user_word
    else:
        return valid_words[min_index]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    if limit == -1:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return max(len(goal), len(start))
    elif start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    elif start[0] != goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit - 1) + 1
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    if limit == -1: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return max(len(start), len(goal))
        # END
    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)
    else:
        add_diff = meowstake_matches(start, goal[1:], limit - 1) # Fill in these lines
        remove_diff = meowstake_matches(start[1:], goal, limit - 1) 
        substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff) + 1
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for p in zip(typed,prompt):
        if p[0] == p[1]:
            count += 1
        else:
            break
    process = count / len(prompt)
    # print_progress({'id': 1, 'progress': 0.6})
    send({'id': id, 'progress': process})
    return process
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report

from operator import sub
def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for timesi in times_per_player:
        pair = [(x, y) for x,y in zip(timesi[1:], timesi[0:])]
        amount_time = [sub(pair[i][0],pair[i][1]) for i in range(len(pair))]
        times += [amount_time]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    """
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 2]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
    [['What'], ['great', 'luck']] 

    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 3]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
    [['What', 'luck'], ['great']]         

    >>> p2 = [4, 3, 1]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
    [['What'], ['great'], ['luck']]         
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # res = [['']] * len(all_times(game))
    res = [[] for _ in players]
    for index_word in words:
        word = word_at(game, index_word)
        list_word_time = []
        for index_player in players:
            word_time = time(game, index_player, index_word)
            list_word_time += [word_time]
        # index_player, _ = min([pair for pair in zip(players, list_word_time)], key=lambda item: item[1])
        index_player = list_word_time.index(min(list_word_time))
        res[index_player] += [word]
    return res
    # END PROBLEM 10



def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]

def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""
    """
	>>> distances = get_key_distances()
	>>> distances["a", "a"]
	0.0
	>>> distances["a", "d"] # 2.0 / 9
	2.0
    """
    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"
    if limit == -1:
        return float('inf')
    elif len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = key_distance_diff(start, goal[1:], limit - 1) + 1
        remove_diff = key_distance_diff(start[1:], goal, limit - 1) + 1
        substitute_diff = key_distance_diff(start[1:], goal[1:], limit - 1) + key_distance[start[0], goal[0]]
        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1


def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized
#arg是元组
#*arg是本身

key_distance_diff = memo(key_distance_diff)#mycode
key_distance_diff = count(key_distance_diff)

def memo_f_a(f):
    """A memoization function as seen in John Denero's lecture on Growth"""
    cache = {}
    def memoized(user_word, valid_words, diff_function, limit):
        valid_words = tuple(valid_words)
        args = tuple([user_word, valid_words, diff_function, limit])
        if args not in cache:
            cache[args] = f(user_word, list(valid_words), diff_function, limit)
        return cache[args]
    return memoized

def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""
    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    pass
    # END PROBLEM EC2
faster_autocorrect = memo_f_a(autocorrect)
##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)

"""
"***test10***"
p0 = [2, 2, 3]
p1 = [6, 1, 2]
g1 = game(['What', 'great', 'luck'], [p0, p1])
players = range(len(all_times(g1)))  # An index for each player
words = range(len(all_words(g1)))    # An index for each word
print([a for a in players])
print([a for a in words])
"***test10***"
"""


"""
"***testec1***"
a_word = 'e'
a_goal = 'q'
print(key_distance[a_word[0], a_goal[0]])
"""