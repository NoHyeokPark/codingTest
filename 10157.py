c, r = map(int, input().split())
cnt = int(input())
arr = [[0 for _ in range(c)] for _ in range(r)]
vec = [(0,1),(1,0),(0,-1),(-1,0)]
x = y = i = 0
cur = 0
def check(x, y):
    if 0<= x < c and 0<= y < r and arr[y][x] != 1:
        return True
    return False
while True:
    i += 1
    if i > c*r:
        print(0)
        break
    if cnt == i:
        print(f"{x+1} {y+1}")
        break
    arr[y][x] = 1
    a, b = vec[cur]
    nx, ny = x+a, y+b
    if check(nx, ny):
        x = nx
        y = ny
    else:
        cur += 1
        cur %= 4
        a, b = vec[cur]
        x += a
        y += b
    