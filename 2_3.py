def adder(*args):
    return sum(map(lambda x: x * x, args))


print adder(1, 2, 3, 4, 5)
