
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t,s = map(int, input().split())
    
    li = list(map(int, input().split()))
    
    ans = 0
    for i in range(s - 1):
        current = li[i]
        next = li[i+1]
        
        default = current + 1 if current < t else 1
        
        diff = abs(next - default)
        cost = min(diff, t - diff)
        ans += cost
    
    print(ans)

