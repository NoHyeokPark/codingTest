n = int(input())
a = map(int, input().split())
cnt = 1    
stack = []
for x in a:
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt+=1
    stack.append(x)
while stack:
    if stack[-1] == cnt:
        stack.pop()
        cnt+=1
    else:
        print('Sad')
        break
else:
    print('Nice')        