arr = []
cnt = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort(key=lambda x:(x[1], x[0]))
k = 0
for i in range(len(arr)):
    if arr[i][0] >= k:
        k = arr[i][1]
        cnt += 1
print(cnt)        
        
