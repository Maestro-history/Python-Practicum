a = input()
b = sorted([int(j) for j in a])
if 0 in b:
    print(str(b[1]) + '0', str(b[-1]) + str(b[-2]))
else:
    print(str(b[0]) + str(b[1]), str(b[-1]) + str(b[-2]))
    
