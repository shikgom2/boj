import sys
input = sys.stdin.readline

while True:
    n = list(map(str, input().split()))
    if len(n) == 0 or n[0] == '0':
        break

    li = int(n[0])
    prob = [0.0] * 1001
    prob[0] = 1.0

    for i in range(1, li + 1):
        m = int(n[i][1:])
        new_prob = [0.0] * 1001
        for j in range(1001):
            for k in range(1, m + 1):
                if j >= k:
                    new_prob[j] += prob[j - k] * 1.0 / m
        prob = new_prob

    x = int(n[-1])
    print(f"{prob[x]:.5f}")