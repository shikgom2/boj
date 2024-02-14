def solve(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    
    return abs(area) / 2

cnt = int(input())
sum = 0
while(True):
    cnt = cnt - 1

    N = int(input())
    vertices = []
    while(True):
        N = N-1
        a, b = map(int, input().split())
        vertices.append((a,b))
        if(N == 0):
            break
    sum = sum + solve(vertices)
    if(cnt == 0):
        break
    
print(int(sum))