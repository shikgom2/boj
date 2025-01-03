import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li1 = list(map(int, input().split()))  # A 배열
li2 = list(map(int, input().split()))  # B 배열

mx = max(li1)
lo = li1.index(mx)
hi = n-1 - list(reversed(li1)).index(mx)

print((sum(li1) + mx*(m-1)) * 10**9 
      + sum(li2) 
      + li2[0]*lo 
      + max(li2)*(hi-lo) 
      + li2[-1]*(n-1-hi))
