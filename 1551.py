n,k = map(int, input().split())
li = input()

start = 0
end = 0

n = []
for i in range(len(li)):

    if(li[i] == ','):
      n.append(int(li[start:end+1]))
      start = i+1  
    else:
        end = i
    
    if(i == len(li) - 1):
       n.append(int(li[start:end+1]))

end = len(n)
tmp = len(n)
for a in range(k):
    for i in range(1, tmp):
        n.append(n[i] - n[i-1])

    del n[0 : (end - a)]
    tmp -= 1

print(*n, sep=',')
