n, m = map(int, input().split())
s = input().split()
dic = {}
ans = 0
i = 0
b = 0
cnt = 0
while i < n:
    if s[i] not in dic:
        dic[s[i]] = 0
    if dic[s[i]] < m:
        dic[s[i]] += 1
        i += 1 
        cnt += 1
        ans = max(ans, cnt) 
    else:
        dic[s[b]] -= 1
        b += 1 
        cnt -= 1     
print(ans)
