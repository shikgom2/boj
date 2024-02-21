MOD = 100

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

x, y, a0, a1, n = map(int, input().split())

if(n == 0):
    if(a0 < 10 and a0 > -10):
        print("0", end="")
    print(a0)
elif(n == 1):
    if(a1 < 10 and a1 > -10):
        print("0", end="")
    print(a1)
else:
    mat = [[x,y], [1,0]]
    result = pow(mat, n-1)

    result = (result[0][0] * a1 + result[0][1] * a0) % MOD  
    if(result < 0):
       print("-",end="")
       result *= -1

    if(result < 10 and result > -10):
       print("0", end = "")
    print(result)
