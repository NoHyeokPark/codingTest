y,x = map(int, input().split())
arr = [[True]*y,[True]*x]
for i in range(y):
    for j, e in enumerate(input()):
        if e == 'X':
            arr[0][i] = False
            arr[1][j] = False
print(max(sum(arr[0]), sum(arr[1])))
