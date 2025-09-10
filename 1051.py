y, x = map(int, input().split())
sq = [input() for _ in range(y)]
vec = [(0,1),(1,0),(1,1)]
ans = 0
for i in range(y):
    for j in range(x):
        n = sq[i][j]
        siz = 1
        while i+siz < y and j+siz < x:
            for dx, dy in vec:
                nx = dx * siz
                ny = dy * siz
                if n != sq[i+ny][j+nx]:
                    break
            else:
                if ans < siz:
                    ans = siz
            siz += 1
print((ans+1)**2)            