from collections import deque
def rain(arr, siz):
    ans = [1]
    vec = [(1, 0),(-1, 0),(0, 1),(0, -1)]
    for i in range(1,100):
        visit = [[True]*siz for _ in range(siz)]
        cnt = 0
        for y in range(siz):
            for x in range(siz):
                if area[y][x] > i and visit[y][x]:
                    cnt += 1
                    q = deque([(y, x)])
                    visit[y][x] = False
                    while q:
                        a, b = q.popleft()
                        for dy, dx in vec:
                            ny = a + dy
                            nx = b + dx
                            if 0 <= ny < siz and 0 <= nx < siz and visit[ny][nx] and area[ny][nx] > i:
                                visit[ny][nx] = False
                                q.append((ny, nx))
        ans.append(cnt)                        
    print(ans)
    return ans                                
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
print(max(rain(area, n)))