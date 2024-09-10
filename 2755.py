import sys
input = sys.stdin.readline

n = int(input())
sum = 0
score = 0

for _ in range(n):
    li = list(map(str, input().split()))
    s = int(li[1])
    sum += s

    if(li[2] == 'A+'):
        score += (4.3 * s)
    elif(li[2] == 'A0'):
        score += (4.0 * s)
    elif(li[2] == 'A-'):
        score += (3.7 * s)
    elif(li[2] == 'B+'):
        score += (3.3 * s)
    elif(li[2] == 'B0'):
        score += (3.0 * s)
    elif(li[2] == 'B-'):
        score += (2.7 * s)
    elif(li[2] == 'C+'):
        score += (2.3 * s)
    elif(li[2] == 'C0'):
        score += (2.0 * s)
    elif(li[2] == 'C-'):
        score += (1.7 * s)
    elif(li[2] == 'D+'):
        score += (1.3 * s)
    elif(li[2] == 'D0'):
        score += (1.0 * s)
    elif(li[2] == 'D-'):
        score += (0.7 * s)

print("%.2f" % ((score / sum) + 0.000000000001))

