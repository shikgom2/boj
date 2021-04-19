#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

long long dp[9]
long long tmp[9];

int main() {
	int n;
	long long div = 1000000007;
	cin >> n;
	dp[1] = 1;
	for(int j = 2; j<= 8; j++)
	{
		dp[j] = 0;
	}	
	
	
	for(int i = 1; i<= n ;i++)
	{
		tmp[1] = (dp[2] + dp[3]) % div;
		tmp[2] = (dp[1] + dp[3] + dp[4]) % div;
		tmp[3] = (dp[1] + dp[2] + dp[4] + dp[5]) % div;
		tmp[4] = (dp[2] + dp[3] + dp[5] + dp[6]) % div;
		tmp[5] = (dp[3] + dp[4] + dp[6] + dp[7]) % div;
		tmp[6] = (dp[4] + dp[5] + dp[8]) % div;
		tmp[7] = (dp[5] + dp[8]) % div;
		tmp[8] = (dp[6] + dp[7]) % div;
		
		for(int j = 1; j<= 8; j++)
		{
			dp[j] = tmp[j];
		}
	}
	cout << dp[1];
    return 0;
}
