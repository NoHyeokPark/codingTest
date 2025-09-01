n = int(input())
buildings = list(map(int, input().split()))
ans = 0
debug = []
for i in range(n):
    cnt = 0
    grad = float('-inf')
    for j in range(i,0, -1):
        p = j-1
        g = (buildings[p] - buildings[i]) / (i-p)
        if g > grad:
            cnt += 1
            grad = g
    grad = float('-inf')        
    for j in range(i,n-1):
        p = j+1
        g = (buildings[p] - buildings[i]) / (p-i)
        if g > grad:
            cnt += 1
            grad = g
    debug.append(cnt)        
    if ans < cnt:
        ans = cnt
print(ans)
print(debug)        