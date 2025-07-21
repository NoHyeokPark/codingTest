n, m = map(int, input().split())
tree = list(map(int, input().split()))
l, r = 0, max(tree)
while l <= r:
    mid = (l+r)//2
    ans = sum(max(0, h-mid) for h in tree)
    if ans >= m:
        l = mid + 1
    else:
        r = mid - 1
print(r)            