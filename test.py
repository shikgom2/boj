def min_cost_to_form_string(t, bags):
    n = len(t)
    dp = [[float('inf')] * (n + 1) for _ in range(len(bags) + 1)]
    dp[0][0] = 0  # Base case: cost of forming empty string is 0
    
    for i in range(1, len(bags) + 1):
        for j in range(n + 1):
            # Case 1: Skip the current bag
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            # Case 2: Use a string from the current bag
            for string in bags[i-1]:
                if j + len(string) <= n and t.startswith(string, j):
                    dp[i][j + len(string)] = min(dp[i][j + len(string)], dp[i-1][j] + 1)
    
    return dp[len(bags)][n] if dp[len(bags)][n] != float('inf') else -1

# Input processing
t = input().strip()
n = int(input().strip())
bags = []
for _ in range(n):
    bag_info = input().strip().split()
    a_i = int(bag_info[0])
    bags.append(bag_info[1:])

# Solve the problem
min_cost = min_cost_to_form_string(t, bags)
print(min_cost)