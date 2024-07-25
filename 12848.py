def check(li, idx, s, e):
    for x in range(s, e):
        #print("check li", idx, zzzzzz)
        if(x == m):
            return False
        if li[idx][x] != '.':
            return False
    return True

n,m = map(int, input().split())

graph = []
for _ in range(n):
    li = list(map(str, input().rstrip()))
    graph.append(li)
k = int(input())
li = list(map(int, input().split()))

grundy = [0] * len(li)

for a in range(k): #check
    for i in range(n):
        for j in range(m):
            e = j + li[a]
            if(check(graph, i, j, e)):
                grundy[a] += 1
                #print("It can!")
ans = 0
for i in range(len(grundy)):
    ans = ans ^ grundy[i]

#print(grundy)
if(ans):
    print("nein")
else:
    print("hyo123bin")