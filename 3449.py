import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li1=  list(map(str, input().rstrip()))
    li2 = list(map(str, input().rstrip()))
    ans = 0
    for i in range(len(li1)):
        if(li1[i] != li2[i]):
            ans += 1
    print(f"Hamming distance is {ans}.")