import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    a = input().strip()
    while True:
        if '()' in a: 
            a = a.replace("()","")
        else: break

    if len(a) == 0: print("YES")
    else: print('NO')