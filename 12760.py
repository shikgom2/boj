import sys
input = sys.stdin.readline 

n, m = map(int, input().split())

li = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    li.append(arr)

scores = [0] * n

for t in range(m):
    round_li = [li[i][t] for i in range(n)]
    
    max_card = max(round_li)
    
    for i in range(n):
        if round_li[i] == max_card:
            scores[i] += 1

max_score = max(scores)
ans = [i+1 for i, score in enumerate(scores) if score == max_score]

print(*ans)
