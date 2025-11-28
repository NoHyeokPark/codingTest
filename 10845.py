import sys
from collections import deque
input = sys.stdin.readline
a = deque()
for _ in range(int(input())):
    arg = input().split()
    if len(arg) == 2:
        if arg[0] == 'push':
            a.append(int(arg[1]))
    elif arg[0] == 'pop':
        if a:
            print(a.popleft())
        else:
            print(-1)
    elif arg[0] == 'size':
        print(len(a))
    elif arg[0] == 'empty':
        if a:
            print(0)
        else:
            print(1)
    elif arg[0] == 'front':
        if a:
            print(a[0])
        else:
            print(-1)
    elif arg[0] == 'back':
        if a:
            print(a[-1])
        else:
            print(-1)            