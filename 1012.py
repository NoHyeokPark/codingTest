def baechu(arr, t, wid, hei):
    cnt = 0
    for x in t:
        if arr[x[1]][x[0]] == 1:
            cnt += 1
            s = []
            s.append([x[1], x[0]])
            arr[x[1]][x[0]] = 2
            while s:
                y, x = s.pop(0)            
                for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < hei and 0 <= nx < wid and arr[ny][nx] == 1:
                        arr[ny][nx] = 2
                        s.append([ny, nx])
    return(cnt)                                
r = int(input())
for _ in range(r):
    x, y, n = map(int, input().split())
    bat = [[0] * x for _ in range(y)]
    t = []
    for _ in range(n):
        x1, y1 = map(int, input().split())
        bat[y1][x1] = 1
        t.append([x1, y1])
    print(baechu(bat, t, x, y) )   