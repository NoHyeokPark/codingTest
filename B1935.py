n = int(input())
op = input()
num =[]
stack = []
for _ in range(n):
    num.append(int(input()))   
for char in op:
    if 'A'<= char <= "Z":
        stack.append(num[ord(char)-ord('A')])
    else:
        temp2 = stack.pop()
        temp1 = stack.pop()
        if char == '+':
            stack.append(temp1 + temp2)
        elif char == '-':
            stack.append(temp1 - temp2)
        elif char == '*':
            stack.append(temp1 * temp2)
        elif char == '/':
            stack.append(temp1 / temp2)
        elif char == '%':
            stack.append(temp1 % temp2)
print(f'{stack.pop():.2f}')   