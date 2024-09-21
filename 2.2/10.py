a = input()
c = int(a[0]) + int(a[1])
b = int(a[-1]) + int(a[-2])
if b > c:
    print(str(b) + str(c))
else:
    print(str(c) + str(b))
