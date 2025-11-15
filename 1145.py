arr = [int(x) for x in input().split()]
arr.sort()
for i in range(arr[0], 970201):
    cnt = 0
    for x in arr:
        if i%x == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break