import sys
input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

li1.sort(reverse=True)
li2.sort(reverse=True)

if li2[0] > li1[0]:
    print(-1)
else:
    ans = 0
    pos = [0] * n
    loaded = 0

    while loaded < m:
        for i in range(n):
            while pos[i] < m:
                if li2[pos[i]] <= li1[i]:
                    loaded += 1
                    pos[i] += 1
                    break
                pos[i] += 1
        ans += 1
    print(ans)