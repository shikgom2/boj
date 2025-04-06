import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    word = input()
    mp = {}
    val = 0
    li = []
    for ch in word:
        if ch not in mp:
            mp[ch] = val
            val += 1
        li.append(mp[ch])
    li = tuple(li)
    if li not in dic:
        dic[li] = {}
    dic[li][word] = dic[li].get(word, 0) + 1

ans = 0
for li in dic:
    tot = sum(dic[li].values())
    all_pairs = tot * (tot - 1) // 2
    same = 0
    for word in dic[li]:
        count = dic[li][word]
        same += count * (count - 1) // 2
    ans += (all_pairs - same)
print(ans)