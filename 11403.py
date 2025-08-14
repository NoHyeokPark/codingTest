n = int(input())
node = [[] for _ in range(n)]
ans = [[0]*n for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            node[i].append(j)        
for i in range(n):
    q = []
    q.extend(node[i])
    while q:
        x = q.pop()
        if ans[i][x] == 0:
            ans[i][x] = 1
            q.extend(node[x])
for b in ans:
    print(' '.join(str(c) for c in b))
