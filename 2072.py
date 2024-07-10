
def check(arr, r, c, color):
    DR = [0, 0, -1, 1, -1, 1, -1, 1]
    DC = [1, -1, 0, 0, -1, 1, 1, -1]
    cnt = [1] * 4
    
    for d in range(8):
        steps = 1
        while True:
            a = r + DR[d] * steps
            b = c + DC[d] * steps
            if 0 <= a < len(li) and 0 <= b < len(li[0]) and li[a][b] == color:
                cnt[d//2] += 1
                steps += 1
            else:
                break
            
    for i in range(4):
        if cnt[i] == 5:
            return True
    return False

n = int(input())
if n < 9:
    print(-1)
    exit()

li = [[0] * 20 for _ in range(20)]

for i in range(n):
    a, b = map(int, input().split())
    li[a][b] = i % 2 + 1
    if i >= 8:
        if check(li, a, b, i % 2 + 1):
            print(i + 1)
            exit()
        
print(-1)