t1, m1, t2, m2 = map(int, input().split())
t1 = t1 * 60 + m1
t2 = t2 * 60 + m2
if t1 > t2:
    t2 += 1440
print((t2 - t1), (t2 - t1) // 30)