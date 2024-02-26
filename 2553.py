N = int(input())
num = 0
tn = N
while tn:
  num += tn//5
  tn //= 5

result = 1
for i in range(1,N+1):
  ti = i
  while ti % 5 == 0:
    ti //= 5
  if num and ti % 2 == 0:
    num -= 1
    ti //= 2
  result = (result*ti) % 10
print(result)