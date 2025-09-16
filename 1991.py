n = int(input())
i2a = {x:i for i, x in enumerate('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split())}
arr = [[] for _ in range(26)]
for _ in range(n):
    a, *b = map(str, input().split())
    for x in b:
        arr[i2a[a]].append(x)
def pre(node):
    print(node, end='')
    for x in arr[i2a[node]]:
        if x != '.':
            pre(x)
def mid(node):
    if arr[i2a[node]][0] != '.':
        mid(arr[i2a[node]][0])
    print(node, end='')
    if arr[i2a[node]][1] != '.':
        mid(arr[i2a[node]][1])   

def post(node):
    for x in arr[i2a[node]]:
        if x != '.':
            post(x)
    print(node, end='')        

pre('A')
print()
mid('A')
print()
post('A')