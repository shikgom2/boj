#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

int dp[501][501];
int arr[501][501];
int main() {
	int n;

	cin >> n;
		
	for(int i = 1; i<=n ; i++)
	{
		for(int j = 1; j<=i; j++)
		{
			cin >> arr[i][j];
		}
	}	
	
	dp[1][1] = arr[1][1];
	
	for(int i = 2; i<=n ; i++)
	{
		for(int j = 1; j<= i; j++)
		{
			if(j == 1)
			{
				dp[i][j] = arr[i][j] + dp[i-1][j];
			}
			else if(j == i)
			{
				dp[i][j] = arr[i][j] + dp[i-1][j-1];
			}
			else{
				int tmp = max(dp[i-1][j-1] , dp[i-1][j]);
				dp[i][j] = arr[i][j] + tmp;
			}
		}
	}
	
	for(int i = 1; i<=n ; i++)
	{
		for(int j = 1; j<=i; j++)
		{
			printf("%d ",dp[i][j]);
		}
		printf("\n");
	}	
	
	int c = 0;
	for(int i = 1; i<=n ; i++)
	{
		c = max(c, dp[n][i]);
	}
	
	cout << c;
    
	return 0;
}
