import sys
input = sys.stdin.readline

N, M = map(int, input().split())
h, m = divmod((M * 1440) // N , 60)
print(f"{h:02d}:{m:02d}")