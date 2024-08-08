import sys
input = sys.stdin.readline

k,a,b = map(int, input().split())
# find [a,b] divmod k == 0  
# range is 10^18.. so find o(1)

ans = 0

#always 0 at choco
if(a<=0 and 0<=b):
    ans += 1 # count 0
    ans += (abs(a) // k)
    ans += (abs(b) // k)
#no choco at 0 (-~- or +~+)
else:
    #swap range
    if(a < 0 and b < 0):
        a,b = b,a
        
    ans += (abs(b) // k)
    ans -= (abs(a) // k)
    if not (abs(a) % k):
        ans += 1
print(ans)