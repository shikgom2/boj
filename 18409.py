n = int(input())
i = input()
cnt = 0
for a in range(len(i)):
    if(i[a] == 'a' or i[a] == 'e' or i[a] == 'i' or i[a] == 'o' or i[a] == 'u'):
        cnt += 1
print(cnt)