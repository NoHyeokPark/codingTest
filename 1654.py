
def ebun(arr, l, r, m):
    while l <= r:
        mid = (l+r) //2
        s = sum(a // mid for a in arr)
        if s >= m:
            l = mid +1
        else:
            r = mid -1
    return (l+r) //2            
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
r = (sum(arr)*2)//m
print(ebun(arr, 0, r, m))    
