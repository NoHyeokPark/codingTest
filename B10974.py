arr = [x+1 for x in range(int(input()))]
rs = []
def recur(num):
    if num == len(arr):
        print(" ".join(map(str,rs)))
    for x in arr:
        if not x in rs:
            rs.append(x)
            recur(num+1)
            rs.pop()
recur(0)