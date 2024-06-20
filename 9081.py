n = int(input())

for i in range(n):
    a = input()
    li = list(a)
    idx1 = 0 
    idx2 = 0
    for i in range(1, len(li)):
          if li[i-1] < li[i]:
                if idx1 < i:
                    idx1 = i
    for i in range(1, len(li)):
          if li[idx1-1] < li[i] :
                idx2 = i   
    if(idx1 != 0 and idx2 != 0):
        li[idx1-1], li[idx2] = li[idx2], li[idx1-1]
        li[idx1:] = list(reversed(li[idx1:]))
    print(*li, sep='')