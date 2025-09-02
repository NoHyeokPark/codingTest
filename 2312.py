t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    x = 2
    cnt = 0
    while n > 1:        
        if n%x == 0:
            n //= x
            cnt += 1
        else:
            if cnt > 0:
                ans.append((x, cnt))
            cnt = 0
            x += 1         
    ans.append((x, cnt))
    for a, b in ans:
        print(f"{a} {b}")    