s = []
s = list(map(str, input().rstrip()))

check = [0] * 5

for i in s:
    if(i == 'M'):
        check[0] += 1
    elif(i == "O"):
        check[1] += 1
    elif(i == "B"):
        check[2] += 1
    elif(i == "I"):
        check[3] += 1
    elif(i == "S"):
        check[4] += 1

if(check[0] >= 1 and check[1] >= 1 and check[2] >= 1 and check[3] >= 1 and check[4] >= 1):
    print("YES")
else:
    print("NO")