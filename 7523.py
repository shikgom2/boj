import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    a,b = map(int, input().split())
    r = (b-a+1)*(a+b)//2
    print(f'Scenario #{i+1}:\n{r}')
    if i != n-1: print()