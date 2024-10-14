import sys
input = sys.stdin.readline 

k,n,c = map(int, input().split())

li = []
for _ in range(k):
    s, e, m = map(int, input().split())
    li.append([s, e, m])

li.sort(key=lambda x: (x[0], x[1]))

ans = 0
ride_off = []

for cur in li:
    s, e, m = cur
    
    ride_off = [x for x in ride_off if x > s]
    
    while m > 0 and len(ride_off) < c:
        ride_off.append(e)
        ans += 1
        m -= 1

    while m > 0 and ride_off and max(ride_off) > e:
        ride_off.remove(max(ride_off))
        ride_off.append(e)
        m -= 1

print(ans)
