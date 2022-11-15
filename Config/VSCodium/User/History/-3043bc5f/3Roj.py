sign = input("введите действие")
a = input("введите первое число")
b = input("введите второе число")
if (sign == "+"):
    print(ceil(float(a)+float(b)))
elif (sign == "-"):
    print(ceil(float(a)-float(b)))
if (sign == "*"):
    print(ceil(float(a)*float(b)))
elif (sign == "/"):
    print(ceil(float(a)/float(b)))
