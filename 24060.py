def ms(arr, p, r, cnt, k):
    if p < r:
        q = (p+r)//2
        ms(arr, p, q, cnt, k)
        ms(arr, q+1, r, cnt, k)
        merge(arr, p, q, r, cnt, k)

def merge(arr, p, q, r, cnt, k):
    i = p
    j = q+1
    tmp = []
    while i<=q and j<=r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1
    i = p    
    for x in tmp:
        cnt[0] += 1
        arr[i] = x
        i += 1
        if cnt[0] == k:
            print(x)
        
cnt = [0]      
_, m = map(int, input().split())
arr = list(map(int, input().split()))
ms(arr, 0, len(arr)-1, cnt, m)
if cnt[0] < m:
    print(-1)
