import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())

    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))

    li = []
    for i in range(n):
        li.append((li1[i], li2[i]))

    li.sort()
    cv = li[k-1][0]
    a = []

    for first, second in li:
        if first <= cv:
            a.append(second)
    
    a.sort(reverse=True)
    ans = sum(a[:k])
    
    print(cv, ans)