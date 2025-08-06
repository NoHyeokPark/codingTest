from collections import deque

def sup(arr):
    ans = [0 for _ in range(n+1)]
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        for y in arr[x]:
            if ans[y] == 0:
                ans[y] = x
                q.append(y)
    return ans            
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for c in sup(arr)[2:]:
    print(c)