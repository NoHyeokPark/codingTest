from collections import deque
n = int(input())
q = deque()
cur = []
for _ in range(n):
    a = input()
    if a[0] == '1':
        q.append(a[2])
        cur.append(False)
    elif a[0] == '2':
        q.appendleft(a[2])
        cur.append(True)
    elif a[0] == '3':
        if q:
            if cur.pop():
                q.popleft()
            else:
                q.pop()
if q:
    print(''.join(q))
else:
    print(0)                    