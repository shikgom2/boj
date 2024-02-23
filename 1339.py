N = int(input())
wo = [input().rstrip() for _ in range(N)]

dic = {}
for w in wo:
    cnt = len(w)-1
    for ww in w:
        if ww not in dic:
            dic[ww] = pow(10, cnt)
        else:
            dic[ww] += pow(10, cnt)
        cnt -= 1

dic = sorted(dic.values(), reverse=True)

res = 0
num = 9

for v in dic:
    res += v*num
    num -= 1

print(res)