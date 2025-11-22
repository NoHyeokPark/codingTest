for _ in range(int(input())):
    h, w, n = map(int, input().split())
    f = (n-1)%h +1
    b = ((n-1)//h) +1
    print(f"{f}{b:02d}")