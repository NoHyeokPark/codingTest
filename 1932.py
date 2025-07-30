n = int(input())
row = []
for i in range(n):
    col = [0]+list(map(int, input().split())) + [0]
    row.append(col)
for i in range(1,n):
    for j in range(1,i+2):
        row[i][j] += max(row[i-1][j-1], row[i-1][j])
print(max(row[n-1]))        