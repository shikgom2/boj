import sys
input = sys.stdin.readline

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

ans1 = li1[0] * 1 + li1[1] * 2 + li1[2] * 3
ans2 = li2[0] * 1 + li2[1] * 2 + li2[2] * 3

if(ans1 > ans2):
    print(1)
elif(ans1 < ans2):
    print(2)
else:
    print(0)