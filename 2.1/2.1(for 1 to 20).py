#(1)
# print('Привет, Яндекс!')
#
#(2)
#a = input()
#print("Как Вас зовут?")
#print(f"Привет, {a}")
#
#(3)
#f = input()
#for i in range(3):
#    print(f)
#
#(4)
#a = int(input())
#print(a - 95)
#(5)
#a = int(input())
#b = int(input())
#c = int(input())
#print(c - (a * b))
#
#(6)
#a = input()
#b = int(input())
#c = int(input())
#d = int(input())
#print("Чек")
#print(f'{a} - {c}кг - {b}руб/кг')
#print(f'Итого: {c * b}руб')
#print(f'Внесено: {d}руб')
#print(f'Сдача: {d - (c * b)}руб')
#(7)
#N = int(input())
#for i in range(N): 
#    print('Купи слона!')
#(8)
#a = int(input())
#b = input()
#for i in range(a):
#    print(f'Я больше никогда не буду писать \"{b}"!')
#
#(9)
#n = int(input())
#m = int(input()) 
#print(int(m * n * 0.5))
#
#(10)
#name = input()
#age = str(int(input()))
#print(f'Группа №{age[0]}.')
#print(f'{age[-1]}. {name}.')
#print(f'Шкафчик: {age}.')
#print(f'Кроватка: {age[1]}.')
#
#(11)
#a = input()
#print(a[1] + a[0] + a[-1] + a[-2])
#
#(12)
#a = input()
#b = input()
#if len(a) == len(b):
#    pass
#elif len(a) < len(b):
#    a = (len(b) - len(a)) * '0' + a
#elif len(b) < len(a):
#    b = (len(a) - len(b)) * '0' + b
#end = ''
#for i in range(len(a)):
#    end += str(int(a[i]) + int(b[i]))[-1]
#print(end)
#
#(13)
#a = int(input())
#b = int(input())
#print(b // a)
#print(b % a)
#
#(14)
#a = int(input())
#b = int(input())
#c = int(input())
#print(a + c + 1)
#
#(15)
#a = int(input())
#b = int(input())
#c = int(input())
#cur = a * 60 + b + c
#if len(str(cur % 60)) == 1:
#    alpha = f'{(cur // 60) % 24}:0{cur % 60}'
#else:
#    alpha = f'{(cur // 60) % 24}:{cur % 60}'
#if len(alpha) == 4:
#    print('0' + alpha)
#else:
#    print(alpha)
#
#
#(16)
#a = int(input())
#b = int(input())
#c = int(input())
#print(str((b - a) / c) + '0')
#
#
#(17)
#a = int(input())
#b = input()
#print(a + int(b, 2))
#
#(18)
#a = input()
#b = int(input())
#print(b - int(a, 2))
#
#
#(19)
#a = input()
#b = int(input())
#c = int(input())
#d = int(input())
#print('================Чек================')
#r = 35 - 5 - len(f'{a}') - 1
#print(f'Товар:' + ' ' * r + f'{a}')
#r1 = 35 - 5 - len(f'{c}кг * {b}руб/кг')
#print(f'Цена:' + ' ' * r1 + f'{c}кг * {b}руб/кг')
#r2 = 35 - 6 - len(f'{c * b}руб')
#print(f'Итого:' + ' ' * r2 + f'{c * b}руб')
#r3 = 35 - 7 - len(f' {d}руб')
#print(f'Внесено:' + ' ' * r3 + f'{d}руб')
#r4 = 35 - 6 - len(f'{d - c * b}руб')
#print(f'Сдача:' + ' ' * r4 + f'{d - c * b}руб')
#print(f'===================================')
#
#
#(20)
#n = int(input())
#m = int(input())
#k = int(input())
#ka = int(input())
#
#for m1 in range(1, n):
#    if (k - ka) * m1 == (m - ka) * n:
#        print(m1, n - m1)