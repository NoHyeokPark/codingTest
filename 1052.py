n, m = map(int, input().split())
binary = bin(n)[2:]
cnt = 0
for i, b in enumerate(binary):
    if b == '1':
        cnt += 1
        if cnt == m:
            binary = binary[i+1:]
            break
else:
    binary = ''
if '1' in binary:                
    ans = int(''.join('1' if b == '0' else '0' for b in binary), 2) +1
else:
    ans = 0    
print(ans)