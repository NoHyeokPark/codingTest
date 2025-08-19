n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        for x in arr[i]:
            ans[i].append(x)
    else:
        for j in range(3):
            y = arr[i][j] + min(ans[i-1][j-1], ans[i-1][j-2])
            ans[i].append(y)
print(min(ans[n-1]))            
                
            