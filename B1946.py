n = int(input())
for _ in range(n):
    m = int(input())
    p = [list(map(int, input().split())) for _ in range(m)]
    p.sort()
    cut = p[0][1]
    cnt = 1
    for x in p:
        if x[1] < cut:
            cnt +=1
            cut = x[1]
    print(cnt)        
    