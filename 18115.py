from collections import deque
n = int(input())
act = list(map(int, input().split()))
act.reverse()
ans = deque()
for i in range(n):
    x = act[i]
    if x == 1:
        ans.appendleft(i+1)
    elif x == 2:
        ans.insert(1, i+1)
    elif x == 3:
        ans.append(i+1)
print(' '.join(str(x) for x in ans))        