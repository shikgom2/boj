import sys
input = sys.stdin.readline

def test(i, used, usedMe):
    if i == len(digs):
        return True
    if i > len(digs) or digs[i] == 0:
        return False
    if not usedMe and (test(i + 1, used, True) or test(i + 2, used, True)):
        return True
    for j in range(n):
        if not used[j]:
            usedBefore = False
            for k in range(j):
                if not used[k] and d1s[j] == d1s[k] and d10s[j] == d10s[k]:
                    usedBefore = True
                    break
            if usedBefore:
                continue
            if d10s[j] == 0:
                if d1s[j] == digs[i]:
                    used[j] = True
                    if test(i + 1, used, usedMe):
                        return True
                    used[j] = False
            elif i + 1 < len(digs):
                if d10s[j] == digs[i] and d1s[j] == digs[i + 1]:
                    used[j] = True
                    if test(i + 2, used, usedMe):
                        return True
                    used[j] = False
    return False

num = int(input())
n = int(input())
digs = []
tmp = num
while tmp > 0:
    digs.append(tmp % 10)
    tmp //= 10
digs = digs[::-1]

numbers = list(map(int, input().split()))

d10s = [x // 10 for x in numbers]
d1s = [x % 10 for x in numbers]

used = [False] * 25
ans = test(0, used, False)
print(1 if ans else 0)
