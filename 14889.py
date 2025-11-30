n = int(input())
lst = [[int(x) for x in input().split()] for _ in range(n)]
mini = 9999

def cal(l):
    global mini
    t1 = t2 = 0
    l2 = [i for i in range(n) if i not in l]
    for x in l:
        for y in l:
            t1 += lst[x][y]
    for x in l2:
        for y in l2:
            t2 += lst[x][y]
    mini = min(mini, abs(t1 - t2))


def back(l, idx):

    if len(l) >= n//2: 
        cal(l)
        return
    
    for i in range(idx, n):
        l.append(i)
        back(l, i+1)
        l.pop()

back([], 0)
print(mini)
