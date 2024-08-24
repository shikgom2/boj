import sys
input = sys.stdin.readline

li = []
for _ in range(3):
    k = input().rstrip()
    li.append(k)

for i in range(2, -1, -1):
    if(li[i].isdigit()):
        ans = int(li[i]) + (3-i)
        break

if(ans % 15 == 0):
    print("FizzBuzz")
elif(ans % 3 == 0):
    print("Fizz")
elif(ans % 5 == 0):
    print("Buzz")
else:
    print(ans)