import sys
input = sys.stdin.readline 

n=int(input())
if(n%2024==0 and n <= 100000):
    print("Yes")
else:
    print("No")