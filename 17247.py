n,m = map(int, input().split())

x_1, y_1, x_2, y_2 = 0,0,0,0
flag = 0
for i in range(1, n+1):
    li = list(map(int, input().split()))

    for j in range(1, len(li)+1):
        if(flag == 0 and li[j-1] == 1):
            x_1 = i
            y_1 = j
            flag = 1

        elif(flag == 1 and li[j-1] == 1):
            x_2 = i
            y_2 = j
            break

#print(x_1, x_2, y_1, y_2)
print(max(x_1, x_2) - min(x_1, x_2) + max(y_1, y_2) - min(y_1, y_2))