N,m,M,T,R = map(int, input().split())
cnt = 0
ex = 0
h = m
while ex < N:
    if m+T > M:
        cnt = -1
        break
    if (h+T) <= M:
        ex += 1
        h += T
    else:
        h = min(h-R, m)
    cnt += 1
print(cnt)    
    