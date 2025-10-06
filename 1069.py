x, y, d, t = map(int, input().split())
l = (x**2 + y**2)**0.5
if d > t:
    ans = (l//d)*t
    if l//d == 0:
        ans = min(l, t+d-l, 2*t)
    else:
        ans += min(t, l%d)    
else:
    ans = l
print(ans)    