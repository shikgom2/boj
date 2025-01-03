import math
from collections import deque
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, m, k = map(int, input().split())
    li = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    
    # 1. Bob이 만들 수 있는 모든 k장 합 구하기
    bob_sums = []
    def dfs_bob(idx, chosen, total):
        # k장 뽑았으면 합을 bob_sums에 추가
        if chosen == k:
            bob_sums.append(total)
            return
        # idx가 n을 넘어가면 더 뽑을 수 없으므로 종료
        if idx >= n:
            return
        # 현재 카드를 사용하지 않는 경우
        dfs_bob(idx+1, chosen, total)
        # 현재 카드를 사용하는 경우
        dfs_bob(idx+1, chosen+1, total + li[idx])
    
    dfs_bob(0, 0, 0)
    bob_sums.sort()
    
    # 2. Alice가 만들 수 있는 모든 k장 합 구하기
    alice_sums = []
    def dfs_alice(idx, chosen, total):
        if chosen == k:
            alice_sums.append(total)
            return
        if idx >= m:
            return
        dfs_alice(idx+1, chosen, total)
        dfs_alice(idx+1, chosen+1, total + li2[idx])
    
    dfs_alice(0, 0, 0)
    alice_sums.sort()
    
    # 3. |B - A|의 최소값 구하기
    # 방법1) 투포인터
    i, j = 0, 0
    min_diff = math.inf
    while i < len(bob_sums) and j < len(alice_sums):
        b_val = bob_sums[i]
        a_val = alice_sums[j]
        diff = abs(b_val - a_val)
        if diff < min_diff:
            min_diff = diff
        
        # 더 작은 값을 가진 쪽 포인터를 이동
        if b_val < a_val:
            i += 1
        else:
            j += 1
    
    # 방법2) 이진탐색으로도 구할 수 있음
    # 여기서는 투포인터로만 최소값을 구해도 충분합니다.
    
    # 4. |B - A|의 최대값 구하기
    max_bob = bob_sums[-1]  # Bob 점수 중 최대
    min_bob = bob_sums[0]   # Bob 점수 중 최소
    max_alice = alice_sums[-1]
    min_alice = alice_sums[0]
    
    max_diff = max(abs(max_bob - min_alice), abs(min_bob - max_alice))
    
    print(min_diff, max_diff)
