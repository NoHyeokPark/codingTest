n = int(input())
for i in range(n):
    if i % 2 == 1:
        print(' ', end='')
    for j in range(2*n-1):
        if j%2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()        