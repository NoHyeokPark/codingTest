n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
ans = [0] * (n+1)
stk = [1]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
while stk:
    s = stk.pop()
    ans[s] = 1
    for x in arr[s]:
        if ans[x] != 1:
            stk.append(x)
print(sum(ans)-1)         