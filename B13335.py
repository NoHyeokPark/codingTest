n,w,l = map(int,input().split())
t = [[x, 0] for x in list(map(int, input().split()))]
bridge = []
cnt = 0
while True:
    for x in bridge:
        x[1] +=1
    if bridge and bridge[0][1] == w:
        bridge.pop(0)          
    if t and l - sum(row[0] for row in bridge if row) >= t[0][0]:
        bridge.append(t.pop(0))        
    cnt += 1
    if not t and not bridge:
        print(cnt)
        break          
    