w = input()   
arr = [6,2,5,5,4,5,6,3,7,5]
idx = [int(x) for x in w]
num = 0
cnt = 0
def up(n, idx):
    if n < 0:
        return 0
    if idx[n] <9:
        idx[n] += 1
        return arr[idx[n]] - arr[idx[n]-1]
    else:
        idx[n] = 0
        return up(n-1, idx) + 1
while True:
    num += up(len(w)-1, idx)
    if  num == 0:
        break
    else:
        cnt +=1
print(cnt)  