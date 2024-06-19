from collections import Counter

n = int(input())
li = []

for _ in range(n):
    k = int(input())
    li.append(k)

li.sort()

cnt = Counter(li).most_common(2)

print(round(sum(li) / n))
print(li[(n - 1) // 2])
if(n > 1):
    if(cnt[0][1] == cnt[1][1]):
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(li) - min(li))