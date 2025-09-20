arr = [list(map(int, input().split())) for _ in range(9)]
big = -1
idx = (0,0)
for i in range(9):
    for j in range(9):
        if arr[i][j] > big:
            big = arr[i][j]
            idx = (i+1,j+1)
print(big)
print(f"{idx[0]} {idx[1]}")