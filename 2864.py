def greed(c):
    p = m = 0
    x = 1
    while c > 0:
        n = c%10
        if n == 5:
            p += 1 * x
        elif n == 6:
            m += 1 * x
        c = c//10
        x *= 10
    return (p, m)    

a, b = map(int, input().split())
x1, y1 = greed(a)
x2, y2 = greed(b)
print(f'{a + b-y1-y2} {a + b+x1+x2}')
