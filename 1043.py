n, m = map(int, input().split())
trues = list(map(int, input().split()))[1:]
visit = [False for _ in range(n+1)]
line = [set() for _ in range(n+1)]
meet = []
cnt = 0
for y in trues:
    visit[y] = True
for _ in range(m):
    party = tuple(map(int, input().split()[1:]))
    meet.append(party)
    for x in party:
        line[x].update(party)
while trues:
    q = trues.pop()
    for x in line[q]:
        if not visit[x]:
            trues.append(x)
            visit[x] = True
for i, v in enumerate(visit):
    if v:
        trues.append(i)
for m in meet:
    if set(m).isdisjoint(trues):
        cnt += 1
print(cnt)        
    