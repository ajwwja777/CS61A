def f0(a):
    def f1(b):
        if a > b:
            return a
    return f1

a = f0(1)(2)