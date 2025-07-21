str = input()
str2 = str.replace('()','*')
pipe = 0
ans = 0
for char in str2:
    if char == '(':
        pipe += 1
    elif char == ')':
        pipe -= 1
        ans += 1
    elif char == '*':
        ans += pipe
print(ans)        