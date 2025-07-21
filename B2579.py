n = int(input())
arr = [int(input()) for _ in range(n)]
result = [0]
arr.reverse()
def next(cnt, sum, idx, result):
    if idx >= len(arr):
        if sum > result[0]:
            result[0] = sum
        return
    if cnt < 1:
        next(cnt+1, sum+arr[idx], idx+1, result)
    next(0, sum+arr[idx], idx+2, result)
next(0, 0, 0, result)
print(result[0])  