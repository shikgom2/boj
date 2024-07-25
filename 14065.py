import sys
input = sys.stdin.readline

i = float(input().rstrip())
l = 3.785411784
km = 1.609344
ans = l / (i * km) * 100
print(ans)