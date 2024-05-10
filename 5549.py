import sys
input = sys.stdin.readline

n,m=map(int,input().split())
k=int(input())
li=[list(input().rstrip()) for i in range(n)]

J=[[0]*(m+1) for i in range(n+1)]
O=[[0]*(m+1) for i in range(n+1)]
I=[[0]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if li[i-1][j-1]=='J':
            J[i][j]=J[i][j-1]+J[i-1][j]-J[i-1][j-1]+1
            O[i][j]=O[i][j-1]+O[i-1][j]-O[i-1][j-1]
            I[i][j]=I[i][j-1]+I[i-1][j]-I[i-1][j-1]
        elif li[i-1][j-1]=='O':
            J[i][j]=J[i][j-1]+J[i-1][j]-J[i-1][j-1]
            O[i][j]=O[i][j-1]+O[i-1][j]-O[i-1][j-1]+1
            I[i][j]=I[i][j-1]+I[i-1][j]-I[i-1][j-1]
        else:
            J[i][j]=J[i][j-1]+J[i-1][j]-J[i-1][j-1]
            O[i][j]=O[i][j-1]+O[i-1][j]-O[i-1][j-1]
            I[i][j]=I[i][j-1]+I[i-1][j]-I[i-1][j-1]+1

for i in range(k):
    x1, y1, x2, y2=map(int,input().split())

    print(J[x2][y2]-J[x2][y1-1]-J[x1-1][y2]+J[x1-1][y1-1],
          O[x2][y2]-O[x2][y1-1]-O[x1-1][y2]+O[x1-1][y1-1],
          I[x2][y2]-I[x2][y1-1]-I[x1-1][y2]+I[x1-1][y1-1])