import sys
ans = []
temp = []
istr = sys.stdin.readline().rstrip()
for char in istr:
    if char == '<':  
        ans += ' '.join(word[::-1] for word in ''.join(temp).split())
        temp.clear()
    temp += char
    if char == '>':
        ans += temp
        temp.clear()
ans += ' '.join(word[::-1] for word in ''.join(temp).split())
print("".join(ans))