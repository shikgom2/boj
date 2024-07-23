n = int(input())
li = list(map(int, input().split()))
start = input()

grundy = [0] * len(li)
for i in range(n):
    grundy[i] = li[i] - 2

ans = 0
for i in range(n):
    ans = ans ^ grundy[i]
#print(ans, start)

if(ans == 0 and start == 'Whiteking'): #after win
    print("Blackking")
elif(ans == 0 and start == 'Blackking'):
    print("Whiteking")
else:
    print(start)