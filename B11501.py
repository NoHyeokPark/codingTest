import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    ans = 0
    input()
    a = list(map(int, input().split()))
    ma = []
    m = 0
    for x in a[::-1]:
        if m < x:
            m = x
        ma.append(m)
    ma.reverse()    
    for i in range(len(a)):
        ans += ma[i] - a[i]
    print(ans)        
    