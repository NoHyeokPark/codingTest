n = int(input())
myundam = []
ans = 0
for _ in range(n):
    myundam.append(list(map(int, input().split())))
def sk(idx, tf, sal):
    global ans
    if idx == n:
        if sal > ans:
            ans = sal
        return
    if tf == 1 and idx+myundam[idx][0] <= n:
        sk(idx+myundam[idx][0], 1, sal+myundam[idx][1])
        sk(idx+myundam[idx][0], 0, sal+myundam[idx][1])
    else:
        sk(idx+1, 1, sal)
        sk(idx+1, 0, sal)
sk(0,0,0)
sk(0,1,0)
print(ans)