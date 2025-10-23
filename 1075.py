n = int(input())
f = int(input())
n=(n//100)*100
a = (n-(n%f))+f

print(f'{a%100:02d}')
