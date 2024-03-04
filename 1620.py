import sys
input = sys.stdin.readline

def is_number(s):
    return s.strip().isdigit()

n, m = map(int, input().split())
dic = {}

for i in range(1, n + 1):
    s = input().strip()
    dic[s] = i
    dic[i] = s

for i in range(m):
    s = input().strip()
    if is_number(s):
        print(dic[int(s)])
    else:
        print(dic[s])