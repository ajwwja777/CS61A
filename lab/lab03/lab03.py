HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    """
    My example for Pascal's Triangle.
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    My thoughts.
    pascal(row, column) = pascal(row - 1, column) + pascal(row - 1, column - 1)
    """
    if row < 0 or column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)

def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***" 
    """
    注意：
    repeated(compose(f, f), n-1)不可行，f会改变
    """
    if n == 0:
        return lambda x: x
    elif n == 1:
        return f
    elif n > 1:
        return compose1(f, repeated(f, n-1))

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
        return 0
    else:
        return num_eights(x//10) + int(x%10 == 8)

def all_num_eight(n):
    count = 0
    for i in range(1,n):
        if num_eights(i) > 0 or i%8 == 0:
            count += 1
    return count

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    if all_num_eight(n)%2 == 0:
        return pingpong(n-1) + 1#even
    else:
        return pingpong(n-1) - 1#odd
    """
    "*** CODE FROM FLYINGPIG ***"
    def helper(i, state, direction):
        if i == n:
            return state
        if num_eights(i) != 0 or i % 8 == 0:
            return helper(i + 1, state - direction, direction*-1)
        else:
            return helper(i + 1, state + direction, direction)

    return helper(1, 1, 1)
    """
