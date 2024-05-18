a,b,c,d = map(int, input().split())
li = list(map(int, input().split()))

for i in li:
    ans = 0
    if 0 < i % (a + b) <= a:
        ans += 1
    if 0 < i % (c + d) <= c:
        ans += 1
        
    print(ans)