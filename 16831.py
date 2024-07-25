import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)

ans = 0
for i in range(len(li)):
    ans = ans ^ li[i]
if(ans > 1):
    print("Alice")
elif(ans == 1):
    print("Bob")
else:
    flag = True
    for i in range(len(li)):
        if(li[i] % 2 == 1):
            flag = False
            break
    if(flag):
        print("Bob")
    else:
        print("Alice")