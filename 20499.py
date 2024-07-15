s = input()
li = s.split('/')

if(int(li[0]) + int(li[2]) < int(li[1]) or int(li[1]) == 0):
    print("hasu")
else:
    print("gosu")