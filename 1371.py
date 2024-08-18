import sys
input = sys.stdin.read

li = [0] * 26

s = input().replace('\n','').replace(' ','')

for i in range(len(s)):
    li[ord(s[i]) - ord('a')] += 1
ans = []
for i in range(26):
    if(li[i] == max(li)):
        ans.append(chr(i + ord('a')))

print(*ans, sep="")