arr = []
n = int(input())
for x in map(int, input().split()):
    arr.append(x)
arr.sort()
print(arr)
sum = 0
for x in arr:
    sum += x*n
    n -= 1
print(sum)        