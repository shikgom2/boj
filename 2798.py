import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))

val = 10**10
for i in range(0, len(li)):
    for j in range(0, len(li)):
        for k in range(0, len(li)):
            if(i != j and j != k and i != k):
                if(abs(li[i] + li[j] + li[k] - M) < abs(val - M) and li[i] + li[j] + li[k] <= M):
                    val = li[i] + li[j] + li[k]
print(val)