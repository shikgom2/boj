import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
    li = list(map(str, input().rstrip()))
    s = set(li)

    ans = 2015
    li = list(s)
    for i in range(len(li)):
        ans -= ord(li[i])
    print(ans)