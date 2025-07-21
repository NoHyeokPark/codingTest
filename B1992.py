def qurd(x, y, m):
    if m == 1:
        ans.append(arr[x][y])
        return
    for i in range(m):
        for j in range(m):
            if arr[x+i][y+j] != arr[x][y]:
                ans.append('(')
                qurd(x, y, m//2)
                qurd(x, y+m//2, m//2)
                qurd(x+m//2, y, m//2)
                qurd(x+m//2, y+m//2, m//2)
                ans.append(')')
                return
    else:
        ans.append(arr[x][y])
        return
                
ans = []
n = int(input())
arr = [list(c for c in input()) for _ in range(n)]
qurd(0,0,n)
print("".join(ans))
