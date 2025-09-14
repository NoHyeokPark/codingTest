n = input()
arr = ['000','001','010','011','100','101','110','111']
parts = [arr[int(x)] for x in n]
st = ''.join(parts)
a = st.find('1')
print(st[a:])