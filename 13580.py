import sys
input = sys.stdin.readline
li = list(map(int, input().split()))
li.sort()

if(li[2] == li[0] + li[1]):
    print("S")
elif(li[0] == li[1] or li[1] == li[2]):
    print("S")
else:
    print("N")