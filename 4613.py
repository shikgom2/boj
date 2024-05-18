li = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()

while s != '#':
    ans = 0
    for i in range(len(s)):
        ans += li.index(s[i]) * (i+1)
    print(ans)
    s = input()