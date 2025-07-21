chess = []
n, m = map(int, input().split())
for _ in range(n):
    line = list(input())
    chess.append(line)
min = 64        
for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for k in range(8):            
            for l in range(8):
                if (k+l)%2 ==0:
                    if chess[k+i][l+j] == 'W':
                        cnt += 1
                else:        
                    if chess[k+i][l+j] == 'B':
                        cnt += 1
        cnt_r = 64-cnt
        if min > cnt:
            min = cnt
        if min > cnt_r:
            min = cnt_r
print(min)   