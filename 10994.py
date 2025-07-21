n = int(input())-1
arr = [([' ']*(4*n+1)) for _ in range(4*n+1)]
def star(arr, x, y, n):
    if n <= 0:
        return
    for i in range(x,x+n):
        arr[i][y] = '*'
        arr[i][y+n-1] = '*'
    for j in range(y, y+n):
        arr[x][j] = '*'
        arr[x+n-1][j] = '*'
    star(arr, x+2, y+2, n-4)    
star(arr, 0, 0, 4*n+1) 
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end='')
    print()    