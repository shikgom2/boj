import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans1 = 0
ans2 = 0

for i in range(n):
    
    if(li[i] < 30):
        ans1 += 10
    else:
        ans1 += (li[i] // 30 + 1) * 10
        
    if(li[i] < 60):
        ans2 += 15
    else:
        ans2 += (li[i] // 60 + 1) * 15
            
if(ans1 > ans2):
    print(f"M {ans2}")
elif(ans1 < ans2):
    print(f"Y {ans1}")
else:
    print(f"Y M {ans1}")