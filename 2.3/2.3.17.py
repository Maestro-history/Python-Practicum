a = [int(i) for i in input()]
c = ''
for i in a:
    if i % 2 != 0:
        c += str(i)
print(c)
