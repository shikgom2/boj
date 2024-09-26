import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
s = list(map(str, input().rstrip()))

li.sort()
for i in range(3):
    if(s[i] == 'A'):
        print(li[0], end=" ")
    elif(s[i] == 'C'):
        print(li[2],  end=" ")
    else:
        print(li[1], end=" ")