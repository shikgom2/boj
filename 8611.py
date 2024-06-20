def solve(n,i):
    n_num = ''
    while n:
        n_num = str(n%i) + n_num
        n//=i
    
    return n_num

n = int(input())

cnt = 0
for i in range(2,10):
    ans = solve(n,i)
    if (ans == ans[::-1]):
        print(i, ans)
        cnt += 1

n = str(n)
if n == n[::-1]:
    print(10,n)
    cnt += 1

if(cnt == 0):
    print('NIE')