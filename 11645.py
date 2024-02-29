import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    dict = {}
    for i in range(n):
        s = input()

        if s not in dict:            
            dict[s] = True

    print(len(dict))