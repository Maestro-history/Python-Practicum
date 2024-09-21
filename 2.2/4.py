a = int(input())
b = int(input())
c = int(input())
d = {}
d[a] = 'Петя'
d[b] = 'Вася'
d[c] = 'Толя'
vector = reversed(sorted([a, b, c]))
alps = 0
for i in vector:
    alps += 1
    print(f'{alps}. {d[i]}')
