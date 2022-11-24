a = 1
b = 2


def summ(a):
    global b
    return a


# return - принимает в функцию
a = 1
b = 2


def summ():
    global b
    return a


summ(a)
