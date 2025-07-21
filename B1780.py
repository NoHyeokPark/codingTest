m = [0,0,0]
def paper(x, y, n):
    num = arr[x][y]
    if n == 1:
        m[num] += 1
        return
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != num:
                paper(x, y, n//3)
                paper(x+n//3, y, n//3)
                paper(x+2*(n//3), y, n//3)
                paper(x, y+n//3, n//3)
                paper(x+n//3, y+n//3, n//3)
                paper(x+2*(n//3), y+n//3, n//3)
                paper(x, y+2*(n//3), n//3)
                paper(x+n//3, y+2*(n//3), n//3)
                paper(x+2*(n//3), y+2*(n//3), n//3)
                return
    else:
        m[num] += 1    
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
paper(0, 0, n)   
print(m[-1])
print(m[0])
print(m[1])