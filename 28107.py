from collections import defaultdict
n, _= map(int, input().split())
dick = {}
dick = defaultdict(list)
for i in range(1,n+1):
    _, *w = list(map(int, input().split()))
    for x in w:                
        dick[x].append(i)
order = list(map(int, input().split()))
ans = [0 for _ in range(n)]  
for dish in order:
    if dick[dish]:
        t = dick[dish].pop(0)
        ans[t-1] += 1       
print(" ".join(map(str, ans)))           