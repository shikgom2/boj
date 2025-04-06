import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

freq1 = [0] * 26
freq2 = [0] * 26

for ch in s1:
    freq1[ord(ch) - ord('a')] += 1

for ch in s2:
    freq2[ord(ch) - ord('a')] += 1

ans = 0
for i in range(26):
    ans += abs(freq1[i] - freq2[i])

print(ans)
