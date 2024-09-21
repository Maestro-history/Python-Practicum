name1 = input()
name2 = input()
name3 = input()
a = [ord(i) for i in name1]
b = [ord(i) for i in name2]
c = [ord(i) for i in name3]
if c[0] < b[0] and c[0] < a[0]:
    print(name3)
elif b[0] < c[0] and b[0] < a[0]:
    print(name2)
else:
    print(name1)
