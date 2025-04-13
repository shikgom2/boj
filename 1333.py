import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())

tot = N * L + (N - 1) * 5 
song = [False] * tot
for i in range(0, tot, L + 5):
    for j in range(i, i + L):
        song[j] = True
        
for i in range(0, tot, D):
    if not song[i]:
        print(i)
        break
else:
    print(i + D)