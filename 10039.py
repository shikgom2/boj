s = 0
for _ in range(5):
    tmp = int(input())
    if(tmp < 40):
        tmp = 40
    s += tmp
print(int(s/5))