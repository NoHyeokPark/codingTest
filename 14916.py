n = int(input())
ans = n//5
if (n%5)%2 == 0:
    ans += (n%5)//2
else:
    if ans > 0:
        ans += ((n%5)+5)//2 -1
    else:
        ans = -1
print(ans)        