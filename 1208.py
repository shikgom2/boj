import sys
input = sys.stdin.readline

def rightSeq(mid, sum):
    global subsum
    if mid == N:
        if sum in subsum:
            subsum[sum] += 1
        else:
            subsum[sum] = 1
        return
    
    rightSeq(mid + 1, sum + arr[mid])
    rightSeq(mid + 1, sum)

def leftSeq(st, sum):
    global cnt, subsum
    if st == N//2:
        cnt += subsum.get(S - sum, 0)
        return
    
    leftSeq(st + 1, sum + arr[st])
    leftSeq(st + 1, sum)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
subsum = {}
cnt = 0

rightSeq(N//2, 0)
leftSeq(0, 0)

if S == 0: 
    print(cnt - 1)
else: 
    print(cnt)