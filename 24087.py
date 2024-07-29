s = int(input())
a = int(input())
b = int(input())

ans = 250
h = a

while h < s:
    ans += 100
    h += b
print(ans)