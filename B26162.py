prime = [True]*118
ans = []
m = int(118 ** 0.5)
prime[0] = False
prime[1] = False
for i in range(2, m+1):
    if prime[i]:
        for j in range(i*i, 118, i):
            prime[j] = False
for i in range(118): 
    if prime[i]:
        ans.append(i)
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(len(ans)):
        for j in range(len(ans)):
            if ans[i] + ans[j] == n:
                print('Yes')
                break
    else:
        print('No')