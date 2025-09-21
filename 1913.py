n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
x = y = n//2
dx, dy = 1, -1
cnt = 2
arr[y][x] = 1
ans = ''
for i in range(1,n):
    for _ in range(i):
        y += dy
        arr[y][x] = cnt
        cnt += 1
    for _ in range(i):
        x += dx
        arr[y][x] = cnt
        cnt += 1
    dy = -dy
    dx = -dx
else:
    for _ in range(i):
        y += dy
        arr[y][x] = cnt
        cnt += 1
t = int(input())
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
        if arr[i][j] == t:
            ans = f'{i+1} {j+1}'
    print()    
print(ans)    