import sys
input = sys.stdin.readline 

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

n = int(input())
li = list(map(str, input().split()))

bo1 = int(li[0])
bo2 = 1

for i in range(2, len(li), 2):
    val = int(li[i])
    if(val < 0):
        val *= -1
        
    if(li[i-1] == '*'):
        bo1 *= val
    elif(li[i-1] == '/'):
        bo2 *= val
    
    div = gcd(bo1, bo2)
    bo1 //= div
    bo2 //= div

    print(bo1, bo2)
if(bo1 % bo2 == 0):
    print("mint chocolate")
else:
    print("toothpaste")