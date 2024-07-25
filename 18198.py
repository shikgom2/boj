s = input()
a = 0
b = 0
li = ""
for i in s:
    if i == "A":
        li = "A"
    elif i == "B":
        li = "B"
    else:
        if li == "A":
            a += int(i)
        else:
            b += int(i)
if(a>b):
    print("A")
else:
    print("B")