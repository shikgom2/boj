p = int(input())
c = int(input())
ans = p * 50 - c * 10
if p>c:
    ans += 500

print(ans)