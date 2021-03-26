#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

int main() {
	int i;
	int dp[1001][3] = {0,};
	int cost[1001][3];
	cin >> i;
	
	for(int j = 1; j<= i; j++)
	{
		cin >> cost[j][0] >> cost[j][1] >> cost[j][2];
	}
	
	for(int j = 1 ; j <= i ;j++)
	{
		dp[j][0] = min(dp[j-1][1] , dp[j-1][2]) + cost[j][0];
		dp[j][1] = min(dp[j-1][0] , dp[j-1][2]) + cost[j][1];
		dp[j][2] = min(dp[j-1][0] , dp[j-1][1]) + cost[j][2];
	}
	
	cout << min(min(dp[i][0] , dp[i][1]) , dp[i][2]);
    return 0;
}
