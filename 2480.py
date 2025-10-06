arr = [0] * 7
print(arr)
q = list(map(int, input().split()))
while q:
    a = q.pop()
    arr[a] += 1
for i in range(7):
    if arr[i] == 1:
        arr[i] = i*100
    if arr[i] == 2:
        arr[i] = 1000+(i*100)
    if arr[i] == 3:
        arr[i] = 1000*i +10000
print(arr)        
print(max(arr))        