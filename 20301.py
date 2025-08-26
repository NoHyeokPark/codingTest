n, k, m = map(int, input().split())
arr = [i+1 for i in range(n)]
cnt = 0
idx = 0
for _ in range(n):
    if cnt == m :
        cnt = 0
        k = -k
    if k > 0:    
        idx += k-1
    else:
        idx += k    
    idx %= len(arr)
    print(arr.pop(idx))
    cnt += 1
    