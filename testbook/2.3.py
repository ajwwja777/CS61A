empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]
def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def getitem_link1(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    else:
        return getitem_link1(rest(s), i-1)
four = link(1, link(2, link(3, link(4, empty))))
"""
>>> four = link(1, link(2, link(3, link(4, empty))))
>>> four1 = link(1, link(2, link(3, link(4, empty))))
>>> first(four)
1
>>> rest(four)
[2, [3, [4, 'empty']]]
>>> len_link(four)
4
>>> getitem_link(four, 1)
2
"""

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
    

# def apply_to_all_link1(f, s):
#     """Apply f to each element of s."""
#     assert is_link(s)
#     n, i = len_link(s), 0
#     while i < n:
#         f(first(s))
#     return s


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept
        
def keep_if_link1(f, s):
    """mysuccess"""
    assert is_link(s)
    if s == empty:
        return s
    elif f(first(s)) == False:
        return keep_if_link1(f, rest(s))
    else:
        return link(first(s), keep_if_link1(f, rest(s)))
    
def join_link1(s, separator):
    """Return a string of all elements in s separated by separator.
    >>> join_link1(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ''
    else:
        return str(first(s)) + separator + str(join_link1(rest(s), separator)).strip(separator + ' ')
    
def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    
def join_link2(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        kept = join_link2(rest(s), separator)
        return str(first(s)) + separator + str(kept)
    
def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)
    
def print_partitions(n, m):
        lists = partitions(n, m)
        strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))

# >>> print_partitions(6, 4)
"""
empty = 'empty'
def link(first, rest):
    return [first, rest]
def first(s):
    return s[0]
def rest(s):
    return s[1] 
def extend_link(s, t):
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
def apply_to_all_link(f, s):
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
def join_link(s, separator):
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
def partitions(n, m):

    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)
    
def print_partitions(n, m):
        lists = partitions(n, m)
        strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))
print_partitions(2, 2)
"""