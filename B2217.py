n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    arr[-1-i] *= i+1
print(max(arr))    