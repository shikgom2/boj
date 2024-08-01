n = int(input())
li = [i**3 for i in list(map(float, input().split()))]
ans = sum(li) ** (1 / 3)
print(ans)