def solve(n):
    return (n ^ (n - 1)).bit_length()
i,j = map(int, input().split())
i = solve(i)
j = solve(j)
if(i ^ j != 0):
    print("A player wins")
else:
    print("B player wins")