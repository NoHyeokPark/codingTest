n, l = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()
cur = 0
cnt = 0
for x in pipe:
    if x >= cur:
        cur = x+l
        cnt += 1
print(cnt)        