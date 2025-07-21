input()
s = list(map(int, input().split()))
a = [x for x in s]
a = list(set(a))
a.sort()
for x in s:
    for i in range(len(a)):
        if a[i] == x:
            print(i ,end=" ")
            