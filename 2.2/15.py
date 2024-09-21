a = input()
b = input()
end = sorted([int(j) for j in a + b])
print(str(max(end)) + str((end[1] + end[2]) % 10) + str(min(end)))
