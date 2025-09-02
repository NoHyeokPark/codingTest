n = input()
l = len(n)    
num = 10**l + int(n)
arr = [6,2,5,5,4,5,6,3,7,5]
t = 0
cnt = 0
s = str(num)
temp = num
while temp > 9:
    temp, d = divmod(temp, 10)
    t += arr[d]
while True:
    cnt += 1
    num2 = num + cnt
    ans = 0
    while num2 > 9:
        num2, d = divmod(num2, 10)
        ans += arr[d]
    if ans == t:
        break
print(cnt) 