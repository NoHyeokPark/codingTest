from collections import deque
n = int(input())
arr = [[x for x in input()] for _ in range(n)]
visit = [[False]*n for _ in range(n)]
def danji(arr, n):
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '0' or visit[i][j]:
                continue
            visit[i][j] = True    
            q = deque([(i, j)])
            cnt = 0
            while q:
                y, x = q.popleft()
                cnt += 1
                for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n:
                        if not visit[ny][nx] and arr[ny][nx] != '0':
                            visit[ny][nx] = True
                            q.append((ny, nx))
            ans.append(cnt)
    return ans            
ans = danji(arr, n)                
print(len(ans))  
ans.sort()              
for o in ans:
    print(o)