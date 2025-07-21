import sys
input = sys.stdin.readline

st = input().rstrip('\n')
str1 = [x for x in st]
str2 = []
m = int(input())
for _ in range(m):
    s = input().strip()
    if len(s) >1 :
        _, w = s.split()
        str1 += w
    elif s == 'B':
        if str1:
            str1.pop()
    elif s == 'L':
        if str1:
            str2.append(str1.pop())
    elif s == 'D':
        if str2:
            str1.append(str2.pop())
str2.reverse()
print("".join(str1+str2))