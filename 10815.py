n = int(input())
arr = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
result = [[x, i, 0] for i, x in enumerate(numbers)]
arr.sort()
result.sort()
cur1 = 0
cur2 = 0
while cur2 < m and cur1 < n:
    if arr[cur1] < result[cur2][0]:
        cur1 += 1
    elif arr[cur1] > result[cur2][0]:
        cur2 += 1
    else:
        result[cur2][2] = 1
        cur2 += 1
        cur1 += 1
result.sort(key=lambda elem: elem[1])
for i in range(m-1):
    print(result[i][2], end=' ')
print(result[m-1][2])    
