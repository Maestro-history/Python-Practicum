c = [int(input()) for i in range(2)]
a, b = max(c), min(c)


def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return list(reversed(sorted(d)))


for i in f(b):
    if a % i == 0:
        print(i)
        break
else:
    print(1)
