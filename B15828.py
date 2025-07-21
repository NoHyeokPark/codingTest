import sys
n = int(sys.stdin.readline())
arr = []
while True:
    x = int(sys.stdin.readline())
    if x == -1:
        break
    if x == 0:
        arr.pop(0)
    elif len(arr) < n:
        arr.append(x)
print(*arr)