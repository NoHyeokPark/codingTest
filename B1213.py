s = input()
arr = []
wing = []
for x in s:
    if x in arr:
        arr.remove(x)
        wing.append(x)
    else:
        arr.append(x)
if len(arr) > 1:
    print("I'm Sorry Hansoo")
else:
    wing.sort()
    print(''.join(wing + arr + wing[::-1]))    