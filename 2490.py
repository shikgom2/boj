for _ in range(3):
    li = map(int, input().split())
    cnt = 0

    for i in li:
        if(i == 0):
            cnt += 1
    li2 = ["E","A","B","C","D"]
    print(li2[cnt])