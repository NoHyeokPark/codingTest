n = int(input())
sit = input()
cnt = -2
for x in sit:
    if x == 'L':
        cnt += 1
cnt = max(cnt, 0)        
print(n-(cnt//2))        