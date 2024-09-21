
## ЗАРАНЕЕ ИЗВИНЯЮСЬ ЗА ТАКОЙ КОД:))
a = int(input())  # петя
b = int(input())  # вася
c = int(input())  # толя
if a > b and a > c:
    if b < c:
        print(f'          Петя          ')
        print(f'  Толя  ')
        print(f'                  Вася  ')
        print(f'   II      I      III   ')
    else:
        print(f'          Петя          ')
        print(f'  Вася  ')
        print(f'                  Толя  ')
        print(f'   II      I      III   ')

elif b > a and b > c:
    if a > c:
        print(f'          Вася          ')
        print(f'  Петя  ')
        print(f'                  Толя  ')
        print(f'   II      I      III   ')
    else:
        print(f'          Вася          ')
        print(f'  Толя  ')
        print(f'                  Петя  ')
        print(f'   II      I      III   ')


elif c > b and c > a:
    if b > a:
        print(f'          Толя          ')
        print(f'  Вася  ')
        print(f'                  Петя  ')
        print(f'   II      I      III   ')
    else:
        print(f'          Толя         ')
        print(f'  Петя  ')
        print(f'                  Вася  ')
        print(f'   II      I      III   ')
