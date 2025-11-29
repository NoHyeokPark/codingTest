
n = int(input())
arr = list(map( int,input().split()))
idx = [i for i in range(n)]
big = 0

def ab(x):
    return x if x > 0 else -x


def cal(l):
    global big
    num = 0
    for i in range(len(l)-1):
        num += ab(arr[l[i]]-arr[l[i+1]])
    big = max(big, num)
    return    

def back(l):
    if len(l) >= n:
        cal(l)
        return
    for x in idx:
        if x in l:
            continue
        l.append(x)
        back(l)
        l.pop()

back([])
print(big)