import sys
input = sys.stdin.readline

def move(i, j, dir):
    while(True):

        if(li[i][j] == 1 and dir == 'R'):
            dir = 'T'
        elif(li[i][j] == 1 and dir == 'L'):
            dir = 'B'
        elif(li[i][j] == 1 and dir == 'T'):
            dir = 'R'
        elif(li[i][j] == 1 and dir == 'B'):
            dir = 'L'
    
        if(dir == 'R'):
            j += 1
        elif(dir == 'L'):
            j -= 1
        elif(dir == 'T'):
            i -= 1
        elif(dir == 'B'):
            i += 1

        if(i == -1):
            return (0,j,dir)
        elif(i == n):
            return (i-1, j, dir)
        elif(j == -1):
            return(i, 0, dir)
        elif(j == m):
            return (i, j-1, dir)
    

n,m = map(int, input().split())
li = []
for _ in range(n):
    k = list(map(int, input().split()))
    li.append(k)

#if meet mirror
#left -> bottoms
#right -> top
#top -> right
#bottom -> left

#dir order
#right -> top -> left -> bottom
ans = []
#right
for i in range(n):
    dir = "R"
    ans.append(move(i, 0, dir))

#top
for i in range(m):
    dir = "T"
    ans.append(move(n-1, i, dir))

#left
for i in range(n-1, -1, -1):
    dir = "L"
    ans.append(move(i, m-1, dir))

#bottom
for i in range(m-1, -1, -1):
    dir = "B"
    ans.append(move(0, i, dir))

res = []
for i in range(len(ans)):
    #print(ans[i])
    posi, posj, dir = ans[i][0], ans[i][1], ans[i][2]
    #get index
    #if top, always posi = 0
    #0,posj,T -> 2*n + 2*m - posj
    if(dir == 'T'):
        res.append(2*n + 2*m - posj)
    #if bottom, always posi = n-1
    #n-1, posj, B -> n + posj
    elif(dir == 'B'):
        res.append(n + posj + 1)
    #if left, always posj = 0
    #posi, 0, B -> posi+1
    elif(dir == 'L'):
        res.append(posi + 1)
    #if right, alwyas posj = m-1
    #posi, m-1, R -> n+m+posi
    elif(dir == 'R'):
        res.append(n * 2 + m - posi)
print(*res)
