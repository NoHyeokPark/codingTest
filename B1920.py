
n = int(input())
arr = set(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    if x in arr:
        print(1)
    else:
        print(0)    