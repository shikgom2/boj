
li = ["ryytlid", "maagid", "vibulaskjad"]

def sumn(m):
    return m * (m + 1) // 2 

n = int(input())

m = 0
k = 1 << 30 
while k != 0:
    if sumn(m + k) <= n:
        m += k
    k //= 2 

print(li[m % 3])
