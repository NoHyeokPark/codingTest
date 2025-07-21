r = int(input())
for _ in range(r):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = 0
    while True:
            big = max(q)
            for _ in range(q.index(big)):
                q.append(q.pop(0))
                if m == 0:
                    m = len(q)-1
                else:    
                    m -= 1
            if m == 0:
                print(cnt+1)
                break
            else:    
                q.pop(0)
                cnt += 1 
                if m == 0:
                    m = len(q)-1
                else:    
                    m -= 1
