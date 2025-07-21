import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int,input().split()))
card.sort()        
m = int(input())
check = list(map(int,input().split()))
def ejinR(arr, t):
    l = 0
    r = n
    while l < r:
        bi = (l+r)//2    
        if arr[bi] > t:
            r = bi
        else:
            l = bi+1
    return l
def ejinL(arr, t):
    l = 0
    r = n
    while l < r:
        bi = (l+r)//2    
        if arr[bi] >= t:
            r = bi
        else:
            l = bi+1
    return l
ans = []        
for c in check:
    ans.append(ejinR(card, c)-ejinL(card, c))
print(" ".join(map(str, ans)))       