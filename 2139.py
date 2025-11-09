days = [31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    ans = 0
    yun = 0
    a, b, c = map(int, input().split())
    if a+ b+ c == 0:
        break
    if c%4 == 0:
        if c%100 != 0 or c%400 == 0:
            yun = 1
    for i in range(b-1):
        ans += days[i]
    ans += a
    if b > 1:
        ans += yun
    print(ans)    