import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    li = [list(input().rstrip()) for _ in range(R)]
    flag = True
    
    for i in range(R):
        for j in range(C):
            if li[i][j] == '#':
                if i + 1 < R and j + 1 < C and li[i][j+1] == '#' and li[i+1][j] == '#' and li[i+1][j+1] == '#':
                    li[i][j] = '/'
                    li[i][j+1] = '\\'
                    li[i+1][j] = '\\'
                    li[i+1][j+1] = '/'
                else:
                    flag = False
                    break
        if not flag:
            break
    
    print("Case #{}:".format(t))
    if flag:
        for r in li:
            print("".join(r))
    else:
        print("Impossible")
