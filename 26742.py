from collections import defaultdict

li = defaultdict(int)
s = input()

for i in s:
    li[i] += 1

cnt = 0
for val in li.values():
    cnt += val // 2
print(cnt)