x1, x2 = map(int, input().split())
a,b,c,d,e = map(int, input().split())

ans1 = a * (x1**3) / 3 + (b-d) *(x1*x1) / 2 + (c-e) * x1
ans2 = a * (x2**3) / 3 + (b-d) * (x2*x2) / 2 + (c-e) * x2

print(int(ans2-ans1))