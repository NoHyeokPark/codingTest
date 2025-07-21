n = int(input())
dec = []
for _ in range(n):
    s = input().split()
    if len(s) == 2:
        if s[0] == 'push_front':
            dec = [int(s[1])] + dec
        elif s[0] == 'push_back':
            dec.append(int(s[1]))
    elif s[0] == 'pop_front':
        print(dec.pop(0))
    elif s[0] == 'pop_back':
        print(dec.pop())
    elif s[0] == 'size':
        print(len(dec))
    elif s[0] == 'empty':
        if dec:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if dec:
            print(dec[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if dec:
            print(dec[-1])
        else:
            print(-1)
        
        