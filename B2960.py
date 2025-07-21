n, m = map(int, input().split())
cnt = 1
arr = [x for x in range(2,n+1)]
for x in arr:
    de = x
    print(de)
    while de <= n:
        if de in arr:
            if cnt < m:
                arr.remove(de)
                cnt += 1
            else:
                print(de)
                exit(0)
        de += x        