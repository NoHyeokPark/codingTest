for _ in range(int(input())):
    a = b = c = d = 0
    n = int(input())
    a = n//25
    n %= 25
    b = n//10
    n %= 10
    c = n//5
    d = n%5
    print(f'{a} {b} {c} {d}')