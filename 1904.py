n = int(input())
arr = []
arr.append(1)
arr.append(2) 
arr.append(3)  
for i in range(3,n):
    arr.append((arr[i-1]+ arr[i-2])%15746)
print(arr[n-1])    