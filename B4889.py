import sys
input = sys.stdin.readline
while True:
    stack = []
    num = 0
    str = input().rstrip('\n')
    for char in str:
        if char == '-':
            exit(0)
        if char == '{':
            stack.append('{')
        if char == '}':
            if stack:
                stack.pop()
            else:
                stack.append('{')
                num+=1
    num += len(stack)//2
    print(num)            