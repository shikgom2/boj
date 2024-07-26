ans = 0
for _ in range(10):
    k = int(input())
    ans += k
if ans % 4 == 0:
    print("N")
elif ans % 4 == 1:
    print("E")
elif ans % 4 == 2:
    print("S")
else:
    
    print("W")