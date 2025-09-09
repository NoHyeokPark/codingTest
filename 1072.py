import math
x, y = map(int, input().split())
if x == y:
    print(-1)
else:    
    z = (y*100)//x
    n = 1
    while True:
        c = (y+n)*100//(x+n)
        if c > z:
            print(n)
            break
        else:
            n += 1