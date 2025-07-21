str = input()
arr = [int(x) for x in str]
cnt = 1
for i in range(len(arr)):
    if i > 0:
        if arr[i] != arr[i-1]:
            cnt += 1            
print(cnt//2)            