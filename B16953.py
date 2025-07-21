n, m = map(int, input().split())
cnt = 0
while m > n:
    if m%10 == 1:
        m = m//10
        cnt += 1
    elif m%2 == 0:
        m = m/2
        cnt += 1
    else:
        break
if m == n:
    print(cnt+1)
else:
    print(-1)
        