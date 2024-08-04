import sys
input = sys.stdin.readline

# dp[i] = who win?
#dp[2] -> 1 -> 2 -> S lose 
#dp[3] -> 1 -> 2 -> 3 -> F lose 
#dp[4] -> 1 -> 2 -> 4 -> F lose
#dp[5] -> 1 -> 2 -> 4 -> 5 -> S lose
#dp[6] -> 1 -> 2 -> 4 -> 6 -> S lose
#dp[7] -> 1 -> 2 -> 4 -> 6 -> 7 -> F lose
#dp[8] -> 1 -> 2 -> 4 -> 8 -> S lose
#...
n = int(input())
if(n == 2 or n == 6):
    print("Kali")
else:
    print("Ringo")