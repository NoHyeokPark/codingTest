n, m = map(int, input().split())
s = input()
a, c, g, t = map(int, input().split())
dic = {'A':a, 'C':c, 'G':g, 'T':t}
cnt = 0
def check(dic):
    for x in dic.values():
        if x > 0:
            return 0
    return 1
for i in range(n):
    dic[s[i]] -= 1
    if i >= m:
        dic[s[i-m]] += 1
    cnt += check(dic)
print(cnt)        