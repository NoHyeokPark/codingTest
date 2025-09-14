x, y = map(int, input().split())
rate = 100*y // x
if y >= x * 0.99:
    print(-1)    
else:
    l = 0
    r = x
    while l<r:
        mid = (l + r)//2
        ny = mid + y
        nx = mid + x
        nr = ny*100//nx
        if nr > rate:
            r = mid
        else:
            l = mid+1
    print(r)        
                
            
        
        