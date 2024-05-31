n,m = map(int, input().split())
li = [input()[::-1] for _ in range(n)]
print(*li, sep='\n')