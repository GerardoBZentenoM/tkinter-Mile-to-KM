from re import X


def add(*args):
    x = 0
    for n in args:
        x += n
    return x


print(add(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
