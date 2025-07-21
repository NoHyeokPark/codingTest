n, m = map(int, input().split())
order = [int(x) for _ in range(n) for x in input().split()]
print (order)
dish = list(map(int, input().split()))
ans = [ 0 for _ in range(n)]
for x in dish:
    for i in range(n):
        if x in order[n-i-1]:
            order[n-i-1].remove(x)
            ans[i] += 1
            break
print(ans)            
            