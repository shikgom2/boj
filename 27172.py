import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

scores = [0] * 1000001
cards = [0] * 1000001

for i in range(len(li)):
    cards[li[i]] = 1

for i in range(len(li)):
    for j in range(li[i] * 2, 1000001, li[i]):
        if cards[j] == 1:
            scores[li[i]] += 1
            scores[j] -= 1

for i in range(len(li)):
    print(scores[li[i]], end=" ")