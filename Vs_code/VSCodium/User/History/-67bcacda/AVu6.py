a = int(input())
b = int(input())
c = int(input())
if c<b and c<a:
    print(c)
elif a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
elif a<c or b<c:
    print(a)