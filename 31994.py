import sys
input = sys.stdin.readline

li = []
for _ in range(7):
    i,j = list(map(str, input().split()))
    li.append((i,int(j)))

li.sort(key=lambda k : k[1], reverse=True)
print(li[0][0])