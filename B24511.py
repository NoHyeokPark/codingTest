import sys
n = int(sys.stdin.readline())
typ = list(map(int, sys.stdin.readline().split()))
ele = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
q = [ele[i] for i in range(n) if typ[i] == 0]
q.reverse()
q = q + num
print(*q[:m])
        