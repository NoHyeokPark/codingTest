def check(i, arr):
    if arr[i][0] == 0:
        arr[i][0] = 1
        q = [i]
        while q:
            for x in arr[q.pop()][1:]:
                if arr[x][0] == 0:
                    arr[x][0] = 1
                    q.append(x)
        return 1            
    else:
        return 0
n, m = map(int, input().split())
arr = [[0] for _ in range(n+1)]
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,n+1):
    cnt += check(i, arr)
print(cnt)    