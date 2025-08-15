from collections import deque
def area(arr, n, m):
    vec = [(1,0),(-1,0),(0,1),(0,-1)]
    ans = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] ==  0:
                q = deque([(i, j)])
                arr[i][j] =  1
                cnt = 0
                while q:
                    y, x  = q.popleft()
                    cnt += 1
                    for dy, dx in vec:
                        ny = y + dy
                        nx = x + dx
                        if 0<= ny < m and 0 <= nx < n:
                            if arr[ny][nx] == 0:
                                arr[ny][nx] = 1
                                q.append((ny, nx))
                ans.append(cnt)
    return ans            
m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = -1
ans = area(arr, n, m)
ans.sort()
print(len(ans))
print(' '.join(str(c) for c in ans))