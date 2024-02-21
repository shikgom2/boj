MOD = 1000000007

def mul(m1, m2):
  ret = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
  
  for i in range(len(m1)):
    for j in range(len(m2[0])):
      for k in range(len(m1[0])):
        ret[i][j] += m1[i][k]*m2[k][j]
        ret[i][j] %= MOD
    ret[i] = tuple(ret[i])
    
  ret = tuple(ret)
  return ret


def pow(matrix, n):
  if n == 1:
    return matrix
  temp = pow(matrix, n//2)
  ret = mul(temp, temp)
  if n%2 == 1:
    ret = mul(ret, matrix)

  return ret

n = int(input())
m = (
  (0, 1, 1, 0, 0, 0, 0, 0),
  (1, 0, 1, 1, 0, 0, 0, 0),
  (1, 1, 0, 1, 1, 0, 0, 0),
  (0, 1, 1, 0, 1, 1, 0, 0),
  (0, 0, 1, 1, 0, 1, 1, 0),
  (0, 0, 0, 1, 1, 0, 0, 1),
  (0, 0, 0, 0, 1, 0, 0, 1),
  (0, 0, 0, 0, 0, 1, 1, 0)
)

first = ((1,), (0,), (0,), (0,), (0,), (0,), (0,), (0,))

result = mul(pow(m, n), first)
ans = result[0][0]
print(ans)