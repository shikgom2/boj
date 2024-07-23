import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))

    avg = sum(li[1:]) / li[0]
    
    ans = 0
    for i in range(1, len(li)):
        if(avg < li[i]):
            ans += 1

    print(f"{ans/li[0] * 100:.8f}%")