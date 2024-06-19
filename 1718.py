li = []
for i in range(26):
    li.append(chr(i+97))

s = input()
k = input()

key = ''
while True:
    if len(key) > len(s):
        break
    else:
        key += k

v1 = 0
ans = []
for i in range(len(s)):
    try:
        v1 = li.index(s[i]) - li.index(key[i])
        if v1 > 0:
            ans.append(li[v1-1])
        elif v1 <= 0:
            ans.append(li[v1-1])
    except ValueError:
        ans.append(" ")

print(''.join(ans))