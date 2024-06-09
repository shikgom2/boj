import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

check = [0] * (10**6)

if(n > 60):
    print("Yes")
else:
    for x in range(n):
        for y in range(x + 1, n):
            for z in range(y + 1, n):
                for w in range(z + 1, n):
                    if li[x] ^ li[y] ^ li[z] ^ li[w] == 0:
                        print("Yes")
                        exit()

    print("No")
