arr = [1,2,3,5,8]
n = int(input())
for i in range(n):
    if len(arr) <= i:
        arr.append(arr[i-2]+arr[i-1])
print(arr[n-1]%10007)    