import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    mod = 1
    n = int(input())
    li = []
    for i in range(n):
        k = int(input())
        li.append(k)

    while(True):
        s = set()
        for j in range(n):
            s.add(li[j] % mod)
        if(len(s) == n):
            print(mod)
            break
        mod += 1