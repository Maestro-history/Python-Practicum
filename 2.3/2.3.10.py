a = True
x, y = 0, 0
while a != 'india':
    a = input()
    if a == 'СТОП':
        print(y)
        print(x)
        break
    else:
        cord = int(input())
        if a == 'СЕВЕР':
            y += cord
        elif a == 'ЮГ':
            y -= cord
        elif a == 'ЗАПАД':
            x -= cord
        elif a == 'ВОСТОК':
            x += cord
