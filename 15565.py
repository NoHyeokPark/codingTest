n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = n+1
l = 0
r = 0
cnt = 0
while True:
    if cnt < m:
        if r == n:
            break
        if arr[r] == 1:
            cnt += 1
        r += 1
    else:
        ans = min(ans, r-l)
        if arr[l] == 1:
            cnt -= 1
        l += 1 
if ans == n+1:
    ans = -1
print(ans)        