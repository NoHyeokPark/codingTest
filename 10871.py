_, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for a in arr:
    if a < x:
        ans.append(str(a))
print(' '.join(ans))        