a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    print(3)
elif a==b or b==c or a == c:
    print(2)
elif a != b and b != c:
    print(0)