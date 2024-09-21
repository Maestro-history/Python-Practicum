a, cnt = True, 0
while a != 'cat':
    a = float(input())
    if a >= 500:
        cnt += (a * 90) / 100
    elif a == 0:
        print(cnt)
        break
    else:
        cnt += a
