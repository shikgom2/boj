import sys
input = sys.stdin.readline
ans = 0
t = int(input())
for _ in range(t):
    check = [False] * 26

    li = list(map(str, input().rstrip()))
    cur = ""
    flag = True
    for i in range(len(li)):
        if(cur != li[i]):
            idx = ord(li[i]) - 97
            cur = li[i]

            if(check[idx]):
                flag = False
            else:
                check[idx] = True
    
    if(flag):
        print(li)
        ans += 1
print(ans)