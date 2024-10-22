import sys
input = sys.stdin.readline
import bisect

n,m = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

check = [0] * 100001
li2.sort()

for i in range(m):
    check[li2[i]] += 1
    
win = 0
lose = 0
draw = 0

for i in range(n):
    tmp = check[li1[i]]
        
    left = bisect.bisect_left(li2, li1[i])
    #print(left)
    
    win += left
    lose += (m - tmp - left)
    
    draw += tmp
    
print(win, lose, draw)