from math import *
int
a = 2
# float
b = 5.4
# str
c = "mommy"
bool
d = True
d1 = False
print("Children \n hi" + str(a))
# =====================================
print(a + b)
print(b - a)
# =====================================
name = input("Как тебя зовут?")
old = input("Сколько тебе лет?")
print(int(old)+5)
# =====================================
num1 = 5.569
print(round(num1, 1))
print(ceil(num1))
# =====================================
if (num1 == 5):
    print("+")
    print("-")
# ======================================
op = input("Введите плюс или минус : ")
number1 = input("Введите первое число:")
number2 = input("Введите второе число:")
if (op == "+"):
    print(int(number1) + int(number2))
elif (op == "-"):
    print(int(number1) - int(number2))
else:
    print("Выберите правильный символ.")
print(pi)


number0 = 5


def createNum():
    global number0
    number0 = number0**2
    print(number0)


createNum()
