i = int(input())
if (i%4 == 0 or i%400 == 0) and i%100 != 0:
    print("YES")
else:
    print("NO")