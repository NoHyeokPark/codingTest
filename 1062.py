n, k = map(int, input().split())
base = ['a', 'n' ,'t', 'i', 'c']
txts = []
for _ in range(n):
    txt = input()
    txts.append(set([t for t in txt if t not in base]))
all_txts = list(set([ele for txt in txts for ele in txt]))
ans = 0
def back(t_arr, m, idx):
    global ans
    m = max(m, len(all_txts))

    if len(t_arr) == m:
        num = 0
        for txt in txts:
            if txt.issubset(t_arr):
                num += 1
        ans = max(ans, num)
        return
              
    for i in range(idx, len(all_txts)):
        t_arr.add(all_txts[i])
        back(t_arr, m, i+1)
        t_arr.remove(all_txts[i])

if k < 5:
    print(0)
else:
    back(set(), k-5, 0)
    print(ans)