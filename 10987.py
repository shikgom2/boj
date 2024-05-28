ans = 0
a = 'aeiou'
s = input()
for i in range(len(s)):
    if s[i] in a:
        ans+=1
print(ans)