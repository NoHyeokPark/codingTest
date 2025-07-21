n= int(input())
box = []
big = [0, 0]
vol = 0

for i in range(n):
    box.append(list(map(int, input().split())))
    if big[1] < box[i][1]:
        big = box[i]
box.sort()
def parasol (x, y):
    mem = [-1, 0]
    sum = 0
    for z in y:
        if mem[1] <= z[1]:
            sum += mem[1]*(z[0]-mem[0])
            mem = z          
        if x == mem[0]:
            return sum
vol += parasol(big[0], box)
box.reverse()
vol -= parasol(big[0], box)
print(vol+ big[1])
