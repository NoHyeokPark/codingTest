n = int(input())
arr = [int(input()) for _ in range(n)]
ans = []
def dp(ans, i):
    if i ==0:
        ans.append([arr[i],0, 0])
    else:
        ans.append([ans[i-1][2]+arr[i],ans[i-1][0]+arr[i], max(ans[i-1])])
for i in range(n):
    dp(ans, i)
print(max(ans[n-1]))   