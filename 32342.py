import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    S = input().strip()
    cnt = 0
    # 길이가 3 이상일 때만 슬라이딩
    for i in range(len(S) - 2):
        if S[i:i+3] == 'WOW':
            cnt += 1
    print(cnt)
