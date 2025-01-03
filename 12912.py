import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)
