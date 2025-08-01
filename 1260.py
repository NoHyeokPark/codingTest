n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
ans = [0] * (n+1)
stk = [v]
queue = [v]
a1 = []
a2 = []
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for x in arr:
    x.sort()
    x.reverse()    
while stk:
    s = stk.pop()
    if s not in a1:  
        a1.append(s)    
    ans[s] = 1
    for x in arr[s]:
        if ans[x] != 1:
            stk.append(x)   
ans = [0] * (n+1)       
for x in arr:
    x.reverse()                  
while queue:
    s = queue.pop(0)
    if s not in a2:
        a2.append(s)     
    ans[s] = 1
    for x in arr[s]:
        if ans[x] != 1:
            queue.append(x)   
print(' '.join(map(str, a1)))
print(' '.join(map(str, a2)))