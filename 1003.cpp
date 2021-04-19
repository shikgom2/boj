#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

int main() { 
	int i;
	int dp[41][2];
	dp[0][0] = 1;
	dp[0][1] = 0; 
	
	dp[1][0] = 0;
	dp[1][1] = 1;

	cin >> i;
	
	while(i--){
		int k;
		
		cin >> k;
		
		for(int j = 2; j<=k; j++)
		{
			dp[j][0] = dp[j-2][0] + dp[j-1][0];
			dp[j][1] = dp[j-2][1] + dp[j-1][1];
		}
						
		cout << dp[k][0] << " " << dp[k][1] << endl;	
	}
    return 0;
}
