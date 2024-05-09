n,m = map(int, input().split())
score = list(map(int, input().split()))

m_idx = 100000
m_score = 0
for _ in range(m):
    li = list(map(str, input().split()))
    s = 0

    for i in range(len(li)):
        if(li[i] == 'O'):
            s += score[i-1]

    if(m_score < s):
        m_score = s
        m_idx = int(li[0])
    elif(m_score == s):
        m_idx = min(m_idx, int(li[0]))

print(f'{m_idx} {m_score}')