start = input()
a = [int(j) for j in start]
a.sort()
if a[0] + a[-1] == a[1] * 2:
    print('YES')
else:
    print('NO')
