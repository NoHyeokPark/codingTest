

n = int(input())
word = [[] for x in range(n)]
for i in range(n):
    str = input().split()
    for block in str:
        word[i].append(block)
l = input().split()
for ele in l:
    for i in range(n):
        if word[i] and ele == word[i][0]:
            word[i].pop(0)
            break
    else:
        print('Impossible')
        break
else:
    if all(not x for x in word):
        print('Possible')
    else:
        print('Impossible')    