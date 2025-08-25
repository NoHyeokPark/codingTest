from collections import deque


def bfs(grap, target, time):
    ans = [0 for _ in range(len(grap))]
    q = deque([target])
    last = []
    while q:
        idx = q.popleft()
        if grap[idx]:
            for node in grap[idx]:
                if ans[node] < ans[idx]+time[idx]:
                    ans[node] = ans[idx]+time[idx]
                    q.append(node)
        else:
            last.append(idx)
    for i in set(last):
        ans[i] += time[i]         
    return max(ans)           
        
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    grap = [[] for _ in range(n)]
    rgrap = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        rgrap[b-1].append(a-1)
    target = int(input())-1
    print(bfs(rgrap, target, time))