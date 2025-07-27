n = int(input())
arr = [int(input()) for _ in range(n)]
ans = []
def dp(ans, i):
    if i ==0:
        ans.append([arr[i],0])
    elif i == 1:
        ans.append([arr[i],ans[i-1][0]+arr[i]])
    else:
        ans.append([max(ans[i-2])+arr[i],ans[i-1][0]+arr[i]])
for i in range(n):
    dp(ans, i)
print(max(ans[n-1]))    