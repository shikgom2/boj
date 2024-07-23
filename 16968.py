import sys
input = sys.stdin.readline

li = list(map(str, input().rstrip()))

ans = 1
if(li[0] == 'c'):
    ans *= 26
else:
    ans *= 10
    
for i in range(1, len(li)):
    if(li[i] == 'c' and li[i-1] == 'c'):
        ans *= 25
    elif(li[i] == 'c'):
        ans *= 26
    elif(li[i] == 'd' and li[i-1] == 'd'):
        ans *= 9
    elif(li[i] == 'd'):
        ans *= 10

print(ans)