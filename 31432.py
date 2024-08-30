import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

print("YES")
if(n == 0):
    print(0)
else:
    print(li[0] * 111)