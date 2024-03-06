n = input()
cnt = 0
for i in n:
    print(i,end="")
    cnt += 1
    if(cnt == 10):
        print()
        cnt = 0