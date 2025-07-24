n = int(input())
arr = list(map(int, input().split()))
leng = [0 for _ in range(n)]

for i in range(n):
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            leng[i] = max(leng[i], leng[j])
    leng[i]+=1    
print(max(leng))