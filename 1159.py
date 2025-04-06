n = int(input())
li = {}
for _ in range(n):
    s = input().strip()
    if s:
        f = s[0]
        li[f] = li.get(f, 0) + 1

ans = [char for char in sorted(li.keys()) if li[char] >= 5]

if ans:
    print("".join(ans))
else:
    print("PREDAJA")
