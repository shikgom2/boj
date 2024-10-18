import sys
input = sys.stdin.readline 

n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
 
    pow1 = a[0]+a[1]*2+a[2]*3+a[3]*3+a[4]*4+a[5]*10
    pow2 = b[0]+b[1]*2+b[2]*2+b[3]*2+b[4]*3+b[5]*5+b[6]*10
    print('Battle {}: {}'.format(i+1, 'Evil eradicates all trace of Good' if pow2> pow1 else 'Good triumphs over Evil' if pow1 > pow2 else 'No victor on this battle field'))