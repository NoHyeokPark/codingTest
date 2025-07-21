n, m = map(int, input().split())
stack = [[1] for _ in range(6)]
cnt = 0
for _ in range(n):
    i, p = map(int, input().split())
    while p < stack[i][-1]:
        stack[i].pop()
        cnt += 1
    if p > stack[i][-1]:   
        stack[i].append(p)
        cnt += 1
print(cnt)        