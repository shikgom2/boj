import sys
input = sys.stdin.readline
from collections import Counter

li = [int(input().strip()) for _ in range(10)]
counter = Counter(li)

print(sum(li) // 10)
print(counter.most_common(1)[0][0])
