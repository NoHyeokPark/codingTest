s1, s2, s3 = map(int, input().split())
arr = [0 for _ in range(s1+s2+s3+1)]
big = 0
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            x = i+j+k
            arr[x] += 1
            big = max(arr[x], big)
for i in range(len(arr)):
    if arr[i] == big:
        print(i)
        break