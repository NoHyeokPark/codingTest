A, a, B, b, p = map(int, input().split())
ans = 'No'
if A + B <= p:
    ans = 'Yes'
if A > B:
    arr = [A, a]
    m = B
else:
    arr = [B, b]
    m = A
if arr[0]<= p:
    if m <= arr[1]:
        ans = 'Yes'
print(ans) 