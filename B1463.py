import sys
input = sys.stdin.readline

s = [0]*1000001
for i in range(2,1000000):
    s[i] = s[i - 1] + 1
    if i % 2 == 0:
        s[i] = min(s[i], s[i // 2] + 1)
    if i % 3 == 0:
        s[i] = min(s[i], s[i // 3] + 1)
            
n = int(input())
print(s[:n])