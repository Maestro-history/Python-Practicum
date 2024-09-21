a, cnt = True, 0
while a != 'c++':
    a = input()
    if 'зайка' in a:
        cnt += 1
    elif a == 'Приехали!':
        print(cnt)
        break
