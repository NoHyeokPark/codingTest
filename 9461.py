arr = [0 for _ in range(100)]
arr[0:3] = [1,1,1]
def pado(x):
    if arr[x] == 0:
        arr[x] = pado(x-2) + pado(x-3)
    return arr[x]
n = int(input())
for _ in range(n):
    print(pado(int(input())-1))
        