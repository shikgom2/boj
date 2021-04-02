#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

int dp[1516][3];

int main() {
	int n;
	int mod = 1000000007;
	cin >> n;
	
	dp[2][0] = 1;
	dp[2][1] = 1;
	dp[2][2] = 0;
	
	for(int i = 3; i<= n; i++)
	{
		dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod;
		dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod;
		dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod;
	}	

	cout << dp[n][0];
    return 0;
}
