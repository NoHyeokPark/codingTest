from collections import deque
n, k = map(int, input().split())
arr = [0 for _ in range(100001)]
q = deque([n])
while q:
    x = q.popleft()
    if x == k:
        break
    vec = [1, -1, x]
    for dx in vec:
        nx = x + dx
        if 0 <= nx < 100001 and arr[nx] == 0:
            arr[nx] = arr[x]+1
            q.append(nx)
print(arr[k])