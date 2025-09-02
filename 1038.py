arr = []
num = []
n = int(input())
def ms(num, arr, n):
    if flag:
        if len(num) > 0:
            arr.append(num[:])
            if len(arr) >= n:
                flag = False
        if len(num) > 10:
            return
        for j in range(10):
            if not num or j < num[-1]:
                num.append(j)
                ms(num, arr, n)
                num.pop()
ms([], arr, n)   
ans = 0
for x in arr[n-1]:
    ans *= 10 
    ans += x
print(ans)     