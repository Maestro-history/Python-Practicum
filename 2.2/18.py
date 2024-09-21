a = int(input())
b = int(input())
c = int(input())
end = sorted([a, b, c])
if max(end) ** 2 == min(end) ** 2 + end[1] ** 2:
    print('100%')
elif max(end) ** 2 < min(end) ** 2 + end[1] ** 2:
    print('крайне мала')
else:
    print('велика')
