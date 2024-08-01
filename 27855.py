h1,b1 = map(int, input().split())
h2,b2= map(int, input().split())
s1 = 3 * h1 + b1
s2 = 3 * h2 + b2

if s1 > s2:
    print(1, s1 - s2)
elif s1 < s2:
    print(2, s2 - s1)
else:
    print("NO SCORE")