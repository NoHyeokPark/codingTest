from collections import deque
def chess(q, n, c, d):
    arr = [[0]*n for _ in range(n)]
    vec = [(-2, -1), (-1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2)]
    while q:
        a, b = q.popleft()
        if a == c and b == d:
            break
        for dy, dx in vec:
            ny = a + dy
            nx = b + dx
            if 0 <= nx < n and 0 <= ny < n:
                if arr[ny][nx] == 0 or arr[ny][nx] > arr[a][b]+1:
                    arr[ny][nx] = arr[a][b]+1
                    q.append((ny, nx))
    return arr[c][d]
for _ in range(int(input())):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(chess(deque([(a, b)]), n, c, d))
