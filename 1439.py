s = input().strip()

if(len(set(s)) == 1):
   print(0)
   exit()

flag = ''
a = 0
b = 0
for i in s:
    if i == '0' and flag != '0':
        a += 1
        flag = '0'
    elif i == '1' and flag != '1':
        b += 1
        flag = '1'
print(min(a,b))
