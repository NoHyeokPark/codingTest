arr = [0 for _ in range(int(input())+1)]
big = 0
cnt_big = 0    
id1 = 0
id2 = 0        
for i in range(int(input())):
    p, k = map(int, input().split())
    if big < k-p+1:
        big = k-p+1
        id1 = i+1    
    cnt = 0    
    for j in range(p,k+1):
        if arr[j] == 0:
            arr[j] = i+1
            cnt += 1
    if cnt_big < cnt:
        cnt_big = cnt
        id2 = i+1
print(id1)
print(id2)            