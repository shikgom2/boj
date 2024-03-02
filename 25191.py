n = int(input())
i,j = map(int, input().split())
s = (i//2) + j
print(min(s, n))