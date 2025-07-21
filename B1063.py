k, d, n = input().split()
king = [ord(k[0])-ord('A'),int(k[1])-1]
dol = [ord(d[0])-ord('A'),int(d[1])-1]
for _ in range(int(n)):
    s = input()
    if s == 'R':
        if king[0]+1 == dol[0] and king[1] == dol[1]:
            if dol[0]+1 < 8:
                king[0] += 1
                dol[0] += 1
        elif king[0]+1 < 8:
            king[0] += 1
    if s == 'L':
        if king[0]-1 == dol[0] and king[1] == dol[1]:
            if dol[0]-1 >= 0:
                king[0] -= 1
                dol[0] -= 1
        elif king[0]-1 >= 0:
            king[0] -= 1     
    if s == 'B':
        if king[1]-1 == dol[1] and king[0] == dol[0]:
            if dol[1]-1 >= 0:
                king[1] -= 1
                dol[1] -= 1
        elif king[1]-1 >= 0:
            king[1] -= 1     
    if s == 'T':
        if king[1]+1 == dol[1] and king[0] == dol[0]:
            if dol[1]+1 < 8:
                king[1] += 1
                dol[1] += 1
        elif king[1]+1 < 8:
            king[1] += 1
    if s == 'RT':
        if king[1]+1 == dol[1] and king[0]+1 == dol[0]:
            if dol[1]+1 < 8 and dol[0]+1 <8:
                king[0] += 1
                king[1] += 1
                dol[0] += 1
                dol[1] += 1
        elif king[1]+1 < 8 and king[0]+1 <8:
            king[1] += 1
            king[0] += 1 
    if s == 'LT':
        if king[1]+1 == dol[1] and king[0]-1 == dol[0]:
            if dol[1]+1 < 8 and dol[0]-1 >=0:
                king[0] -= 1
                king[1] += 1
                dol[0] -= 1
                dol[1] += 1
        elif king[1]+1 < 8 and king[0]-1 >=0:
            king[1] += 1
            king[0] -= 1 
    if s == 'RB':
        if king[1]-1 == dol[1] and king[0]+1 == dol[0]:
            if dol[1]-1 >= 0 and dol[0]+1 <8:
                king[0] += 1
                king[1] -= 1
                dol[0] += 1
                dol[1] -= 1
        elif king[1]-1 >= 0 and king[0]+1 < 8:
            king[1] -= 1
            king[0] += 1 
    if s == 'LB':
        if king[1]-1 == dol[1] and king[0]-1 == dol[0]:
            if dol[1]-1 >= 0 and dol[0]-1 >=0:
                king[0] -= 1
                king[1] -= 1
                dol[0] -= 1
                dol[1] -= 1
        elif king[1]-1 >= 0 and king[0]-1 >=0:
            king[1] -= 1
            king[0] -= 1  
print(f"{chr(ord('A') + king[0])}{king[1] + 1}")
print(f"{chr(ord('A') + dol[0])}{dol[1] + 1}")