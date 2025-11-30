input()
arr = list(map(int, input().split()))
y = m = 0
for x in arr:
    y += (x//30 +1) * 10
    m += (x//60 +1) * 15
if y == m:
    print(f'Y M {y}')
else:
    print(f"{'Y' if y<m else 'M'} {y if y<m else m}")
    