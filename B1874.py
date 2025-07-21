n = int(input())
s = []
ans = []
str = ""
max = 0
for i in range(n):
    ans.append(int(input()))
for x in ans:  
    while max < x:
        max += 1
        s.append(max)
        str += "+"
    if s.pop() == x:
        str += "-"
    else:
        print('NO')
        break
else:
    for char in str:
        print(char)