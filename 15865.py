import sys
input = sys.stdin.readline 

def hamming(s, t, K):
    cnt = 0
    for i in range(M):
        if s[i] != t[i]:
            cnt += 1
            if cnt > K:
                return
    return


N,M,K = map(int, input().split())

seqs = []
for _ in range(N):
    li = list(map(str, input().rstrip()))
    seqs.append(li)
    
print(seqs)

if K % 2 == 1:
    candidate = seqs[0]
    all_k = True
    ans = -1
    for j in range(1, N):
        d = hamming(candidate, seqs[j], K)
        if d != K:
            all_k = False
        else:
            ans = j
    if all_k:
        print(1)
    else:
        print(ans + 1)
    exit()

subset_size = min(100, N - 1)
for i in range(N):
    candidate = seqs[i]
    quick_ok = True
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if cnt < subset_size:
            if hamming(candidate, seqs[j], K) != K:
                quick_ok = False
                break
            cnt += 1
    if not quick_ok:
        continue
    full_ok = True
    for j in range(N):
        if i == j:
            continue
        if hamming(candidate, seqs[j], K) != K:
            full_ok = False
            break
    if full_ok:
        print(i + 1)
        exit()