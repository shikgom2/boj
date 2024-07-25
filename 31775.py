s1 = input()
s2 = input()
s3 = input()
g = ["k", "l", "p"]
f = [s1[0], s2[0], s3[0]]
f.sort()

if g == f:
    print("GLOBAL")
else:
    print("PONIX")