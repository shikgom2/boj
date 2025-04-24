import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()

    if len(s) > 3:
        rem = int(s[-3:]) % 8
    else:
        rem = int(s) % 8

    if rem != 0:
        print("No")
        continue
    
    m = int(s) // 8
    m = str(m)

    flag = True
    prev = int(m[-1])
    if prev > 8:
        flag = False
    else:
        for i in range(len(m)-2, -1, -1):
            cur = int(m[i])
            if prev < cur:
                flag = False
                break
            prev = cur

    if flag:
        print("Yes")
    else:
        print("No")