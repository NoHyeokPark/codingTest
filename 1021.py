a,b = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [x for x in range(1,a+1)]
ans = 0
p = 0
for x in arr:
    cnt = 0
    while True:
        cnt += 1
        p += 1
        p %= len(arr2)
        if not arr2 or arr2[p] == x:
            break
    ans += min(cnt, len(arr2)-cnt)    
    del arr2[p]
print(ans)    