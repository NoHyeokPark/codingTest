n, m, b = map(int, input().split())
grd = [[int(x) for x in input().split()] for _ in range(n)]
avg = sum(sum(row) for row in grd)//(n*m)

def work(num, b):
    t = 0
    bl = b
    for i in range(n):
        for j in range(m):
            x = grd[i][j] - num
            if x >=0:
                t += x*2
                bl += x
            else:
                t += -x
                bl += x
    if bl < 0:
        return (-1, -1)
    else:
        return (t, num)
    
ans = work(avg, b)
while True:
    avg += 1
    imi = work(avg, b)
    if imi[0] < 0:
        break
    else:    
        if imi[0] <= ans[0]:
            ans = imi
print(f'{ans[0]} {ans[1]}')    
    