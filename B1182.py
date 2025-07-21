def backtrack(arr, m, su, c, cnt):
    if c == len(arr):
        if su == m:
            cnt[0] += 1
        return
    backtrack(arr, m, su+arr[c], c+1, cnt)
    backtrack(arr, m, su, c+1, cnt)

cnt = [0]        
n, m = map(int, input().split())
arr = list(map(int, input().split()))
backtrack(arr, m, 0, 0, cnt)
if m == 0:
    cnt[0] -= 1
print(cnt[0])