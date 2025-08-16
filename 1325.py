
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
ans = [0]
wer = []
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)
def dfs(arr, i):
    visit = [0]*(n+1)
    cnt = 0
    q = [i]
    visit[i] = 1
    while q:
        x = q.pop()
        cnt += 1   
        for v in arr[x]:
            if visit[v] == 0:
                q.append(v)
                visit[v] = 1
    return cnt
for i in range(1, n+1):
    ans.append(dfs(arr, i))
z = max(ans)
for i in range(1,n+1):
    if ans[i] == z:
        wer.append(str(i))
print(ans)        
print(' '.join(wer) )       