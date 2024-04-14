import sys
input = sys.stdin.readline
while(True):
    m = list(map(str, input().strip()))
    if(len(m) == 3 and m[0] == "E" and m[1] == "N" and m[2] == "D"):
        break
    m.reverse()
    print(*m, sep="")