import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    arr = []
    for i in range(0, len(li), 2): 
        arr.append((li[i], li[i+1]))

    arr.sort(key=lambda k : (k[0]))

    weight = [pair[1] for pair in arr]

    ans = 0

    while weight:
        vmin = -10000
        temp = []
        for w in weight:
            if vmin <= w:
                vmin = w
            else:
                temp.append(w)
        weight = temp
        ans += 1
    print(ans)