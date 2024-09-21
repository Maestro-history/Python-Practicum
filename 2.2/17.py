a = float(input())
b = float(input())
c = float(input())

if a != 0:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        if x1 > x2:
            print(round(x2, 2), round(x1, 2))
        else:
            print(round(x1, 2), round(x2, 2))
    elif discr == 0:
        x = -b / (2 * a)
        print(round(x, 2))
    else:
        print("No solution")
if a == 0:
    if a == b == c == 0:
        print("Infinite solutions")
    elif b != 0 and c != 0:
        x1 = (-c) / b
        print(format(x1, '.2f'))
    elif b == 0 and c != 0:
        print("No solution")
    elif b != 0 and c == 0:
        x1 = 0 / b
        print(format(x1, '.2f'))
