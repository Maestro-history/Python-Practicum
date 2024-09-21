a = int(input())


def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return list(reversed(sorted(d)))


if len(f(a)) == 2:
    print('YES')
else:
    print('NO')
