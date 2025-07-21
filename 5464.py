n, m = map(int, input().split())
pay = [int(input()) for _ in range(n)]
wei = [int(input()) for _ in range(m)]
space = [0 for _ in range(n)]
queue = []
sal = 0
for _ in range(2*m):
    x = int(input())
    if x > 0:
        for i in range(n):
            if space[i] == 0:
                space[i] = x
                break
        else:
            queue.append(x)
    else:
        for i in range(n):
            if space[i] == -x:
                sal += wei[space[i]-1]*pay[i]
                space[i] = 0
                if queue:
                    space[i] = queue.pop(0)
                break        
print(sal)                