import sys
input = sys.stdin.readline

n = int(input())
while(True):
    k = int(input())
    if(k==0):
        break
    
    if(k%n == 0):
        print(f"{k} is a multiple of {n}.")
    else:
        print(f"{k} is NOT a multiple of {n}.")