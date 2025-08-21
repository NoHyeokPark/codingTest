n = int(input())

current = [1 for _ in range(10)]
current[0] = 0
print(current)

for _ in range(n-1):
    arr = [0 for _ in range(10)]
    for x in range(10):
        if x != 0:
            arr[x-1] += current[x]
        if x != 9:
            arr[x+1] += current[x]
    current = arr

print(sum(current))