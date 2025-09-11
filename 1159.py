n = int(input())
dick = {}
arr = []
for _ in range(n):
    x = input()[0]
    dick[x] = dick.get(x,0) + 1
for k, v in dick.items():
    if v >= 5:
        arr.append(k)
if arr:        
    arr.sort()
    print(''.join(arr))
else:
    print('PREDAJA')    
        