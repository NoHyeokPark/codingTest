n = int(input())
f = int(input())
n=(n//100)*100
if n%f != 0:
    a = (n-(n%f))+f
else:
    a = 0    
print(f'{a%100:02d}')
