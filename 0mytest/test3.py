a = 1
b = 2
print(a)

def f(x):
    return x + 1
def add_one(x):
    b = 2
    def g(x):
        nonlocal b
        return x
    return f(a)

print(add_one(10))
print(a)