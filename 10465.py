k = int(input())
s = input()

count = [0] * 26
ans = ""
last = ord(s[0])-97
for i in range(k):
    ans += s[i]
    count[ord(s[i])-97] += 1    
for i in range(k, len(s)):
    shift = count.index(max(count))+1
    ans += chr(97+ (ord(s[i]) -97 +shift) % 26)
    count[last] -= 1
    last = ord(s[i-k+1])-97
    count[ord(s[i])-97] += 1

print(ans)