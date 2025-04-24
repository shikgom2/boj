import sys
input = sys.stdin.readline

def solve(li, b):
    li.sort()
    cnt = 0
    tot = 0
    for i in li:
        if tot + i > b:
            break
        tot += i
        cnt += 1
    return cnt

t = int(input())
for i in range(1, t+1):
    n, b = map(int, input().split())
    li = list(map(int, input().split()))
    print(f"Case #{i}: {solve(li, b)}")
