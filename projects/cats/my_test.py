def f(*args):
    args = tuple(tuple([arg]) for arg in args)
    print(args)
#arg是元组
#*arg是本身,多项

def g(x):
    return x
f([1, 2, 3], [1])
f("woll", "well, then", [1], g, 4)
