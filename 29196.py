import sys
input = sys.stdin.readline

n = input().rstrip()
a = n[n.index('.')+1:]
print('YES')
print(int(a), 10**(len(a)))