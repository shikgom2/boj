memo = {}

def dp(i, j, k):
    if(i <= 0 or j <= 0 or k <= 0):
        return 1
    elif(i > 20 or j > 20 or k > 20):
        memo[(i, j, k)] = dp(20, 20, 20) 
    elif(i < j or j < k):
        return dp(i, j, k-1) + dp(i, j-1, k-1) - dp(i, j-1, k)
    else:
        return dp(i-1, j, k) + dp(i-1, j-1, k) + dp(i-1, j, k-1) - dp(i-1, j-1, k-1)

while True:
    i,j,k = map(int, input().split())
    result = 0

    if(i == -1 and j == -1 and k == -1):
        break
    result = dp(i,j,k)

    print(f"w({i}, {j}, {k} = {result})")
