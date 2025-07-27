n = input()
arr = list(map(int, input().split()))
sum = [] 
for i in range(n):
    if i == 0:
        sum.append(arr[i])
        continue
    sum.append(max(sum[i-1], 0)+arr[i])
print(max(sum))        