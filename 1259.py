import math
while True:
    x = input()
    if x == '0':
        break
    l = len(x)    
    for i in range(math.ceil(l//2)):
        if x[i] != x[l-1-i]:
            print('no')
            break
    else:
        print('yes')