import re
n = int(input())
pattern = r"100+1+|01" 
for _ in range(n):
    text = input()
    result = re.findall(pattern, text)
    print(result)  
    if ''.join(result) == text:
        print('YES')
    else:
        print('NO')    