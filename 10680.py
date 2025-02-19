import sys
input = sys.stdin.readline

mod = 1000000007
results = []

while True:
    try:
        line = input().strip()
    except:
        break
    if line == "0":
        break
    A = line
    B = input().strip()
    C = input().strip()
    n = len(A)

    dp = [[0, 0] for _ in range(n+1)]
    dp[0][0] = 1

    for pos in range(n):
        i = n - 1 - pos
        for carry in (0, 1):
            ways = dp[pos][carry]
            if ways == 0:
                continue
            if A[i] == '?':
                if i == 0:
                    choicesA = range(1, 10)
                else:
                    choicesA = range(0, 10)
            else:
                choicesA = [int(A[i])]
            # B[i]에 대해:
            if B[i] == '?':
                if i == 0:
                    choicesB = range(1, 10)
                else:
                    choicesB = range(0, 10)
            else:
                choicesB = [int(B[i])]
            for dA in choicesA:
                for dB in choicesB:
                    s = dA + dB + carry
                    newcarry = s // 10
                    dC = s % 10
                    if C[i] == '?':
                        if i == 0 and dC == 0:
                            continue
                    else:
                        if int(C[i]) != dC:
                            continue
                    dp[pos+1][newcarry] = (dp[pos+1][newcarry] + ways) % mod

    print(dp[n][0] % mod)