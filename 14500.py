def rotate(t):
    tet = []
    for i in t:
        a, b = i
        tet.append((b,-a))
    return tet
def flip(t):
    tet = []
    for i in t:
        a, b = i
        tet.append((a,-b))
    return tet
def in_range(y, x, h, w):
    return 0 <= y < h and 0 <= x < w
def arround(t, h, w):
    big = 0
    for i in range(h):
        for j in range(w):
            cnt = arr[i][j]
            for vec in t:
                y, x = vec
                ny, nx = i + y, j + x
                if in_range(ny, nx, h, w):
                    cnt += arr[ny][nx]
                else:
                    cnt = 0
                    break
            big = max(big, cnt)
    return big                    
h, w = map(int, input().split())
arr = []
tetro = [[(0,1),(0,2),(1,2)],[(0,1),(1,1),(1,2)],[(0,1),(1,1),(0,2)], 
        [(0,1),(0,2),(0,3)], [(0,1),(1,0),(1,1)]]
rf = [(3,1),(1,1),(3,0),(1,0),(0,0)]
ans = 0
for _ in range(h):
    arr.append(list(map(int, input().split())))
for i in range(5):
    block = tetro[i]
    ans = max(ans, arround(block,h,w))
    r, f = rf[i]
    if f == 1:
        ans = max(ans, arround(flip(block),h,w))
    for j in range(r):
        block = rotate(block)
        ans = max(ans, arround(block,h,w))
        if f == 1:
            ans = max(ans, arround(flip(block),h,w))
print(ans)        
    