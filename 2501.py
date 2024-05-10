n,k = map(int, input().split())
li = []
for i in range(1, n+1):
    if(n%i == 0):
        li.append(i)
        
if(len(li) < k):
    print(0)
else:
    print(li[k-1])