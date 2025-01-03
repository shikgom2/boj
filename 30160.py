
import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().split()))

# 누적합 배열 준비 (인덱스 편의 위해 길이 n+1)
PSA = [0]*(n+1)  # PSA[i] = li[0]+...+li[i-1]   (1-based로 보면 a1..a_i)
PSB = [0]*(n+1)  # PSB[i] = 1*a1 + 2*a2 + ... + i*a_i
PSC = [0]*(n+1)  # PSC[i] = 1^2*a1 + 2^2*a2 + ... + i^2*a_i

for i in range(1, n+1):
    PSA[i] = PSA[i-1] + li[i-1]
    PSB[i] = PSB[i-1] + i*li[i-1]
    PSC[i] = PSC[i-1] + (i*i)*li[i-1]

# 결과 계산
result = []
for k in range(1, n+1):
    val = (k+1)**2 * PSA[k] - 2*(k+1)*PSB[k] + PSC[k]
    result.append(str(val))

print(" ".join(result))
