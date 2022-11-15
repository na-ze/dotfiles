a = 1
b = 2


def summ(a):
    global b
    return a


print(b)

summ(a)
