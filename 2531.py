n, _, k, c = map(int, input().split())
list = [int(input()) for _ in range(n)]
max = 0
def event(arr,i):
    t = [arr[(i+j)%n] for j in range(k)]
    t.append(c)
    return len(set(t))
for i in range(n):
    m = event(list,i)
    if m > max:
        max = m
print(max)        