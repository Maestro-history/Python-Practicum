a = input()
b = input()
c = input()
for i in sorted([a, b, c]):
    if 'зайка' in i:
        print(i, len(i))
        break
