arr = [[0] * 30 for _ in range(30)]
def dari(n, m):
    if n == 1:
        return m
    if arr[n][m] == 0:
        sum = 0
        for i in range(m-1):
            if arr[n-1][i+1] == 0:
                arr[n-1][i+1] = dari(n-1, i+1)
            sum += arr[n-1][i+1]
        arr[n][m] = sum    
    return arr[n][m]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dari(n, m))