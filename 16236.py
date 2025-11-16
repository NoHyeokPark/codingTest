from collections import deque
direct = [(-1,0),(0,-1),(0,1),(1,0)]
def check_range(y, x, n):
    return 0 <= y < n and 0 <= x < n
class shark:
    def __init__(self, size, pos, space):
        self.size = size
        self.pos = pos
        self.time = 0
        self.feed = 0
        self.space = space

    def update(self, y, x, l):
        self.space[y][x] = 0
        self.time += l
        self.pos = (y,x)
        self.feed += 1
        if self.feed >= self.size:
            self.feed = 0
            self.size += 1     
        return   
    
    def bfs(self):
        n = len(self.space)
        visit = [[-1] * n for _ in range(n)]
        q = deque([self.pos])
        y, x = self.pos
        visit[y][x] = 0
        fishs = []
        l = None
        while q:
            y, x = q.popleft()
            if self.space[y][x] < self.size and self.space[y][x] != 0:
                if not l:
                    l = visit[y][x]
                if l == visit[y][x]:    
                    fishs.append((y,x))  
            for vec in direct:
                v1, v2 = vec
                ny, nx = y+v1, x+v2
                if check_range(ny, nx, n) and visit[ny][nx] == -1 and self.space[ny][nx] <= self.size:
                    q.append((ny, nx))
                    visit[ny][nx] = visit[y][x] + 1
        if l:
            fishs.sort(key=lambda v: (-v[0],-v[1]))
            y, x = fishs.pop()
            self.update(y,x,l)
            return True    
        else:    
            return False
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = (0,0)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            pos = (i,j)
            arr[i][j] = 0
s = shark(2,pos, arr)
while s.bfs():
    pass
print(s.time)