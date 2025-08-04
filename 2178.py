from collections import deque
n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append([int(c) for c in input()])
def bfs(miro):
    q = deque()
    q.append((0,0))
    vac = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in vac:
            cx = x + dx
            cy = y + dy
            if cx < 0 or cx > n-1 or cy < 0 or cy > m-1:
                continue
            if miro[cx][cy] == 1:
                q.append((cx, cy))
                miro[cx][cy] = miro[x][y]+1
    return miro[n-1][m-1]                    
print(bfs(miro))    
