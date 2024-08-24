t = int(input())
s = input()
ans = 0

for i in range(t):
    ans += (ord(s[i])-96) * (31 ** i)
print(ans % 1234567891)