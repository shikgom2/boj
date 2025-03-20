import sys
input = sys.stdin.readline

name = input().strip()
dic = {}
for ch in name:
    dic[ch] = dic.get(ch, 0) + 1

cnt = 0
for c in dic.values():
    if c % 2 == 1:
        cnt += 1

if cnt > 1:
    print("I'm Sorry Hansoo")
    exit()

hlaf = []
middle = ""
for ch in sorted(dic.keys()):
    cnt = dic[ch]
    if cnt % 2 == 1:
        middle = ch
    hlaf.append(ch * (cnt // 2))

s = "".join(hlaf)
ans = s + middle + s[::-1]
print(ans)

