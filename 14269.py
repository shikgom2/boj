import sys
input = sys.stdin.readline

def solve():    
    li.sort(key= lambda x: [x[1], x[0]])
    
    size = li[0][1]
    index = 1
    ans = 1
    
    while index < len(li):

        if(li[index][0] in dic):
            ans += 1

        if li[index][0] <= size <= li[index][1]:
            index += 1
        else:
            size = li[index][1]
            ans += 1
            index += 1

    return ans

n = int(input())
li = []

dic = {}

for _ in range(n):
    a, b, c = map(int, input().split())

    if a not in dic:
        dic[a] = 1
    
    li.append([a, a])
    li.append([b, c])

print(solve())