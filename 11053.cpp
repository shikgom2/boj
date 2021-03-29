#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

int dp[1001];
int arr[1001];
int main() {
	int n;

	cin >> n;
		
	for(int i = 1; i<=n ; i++)
	{
		cin >> arr[i];
	}	
	
	for(int i = 1; i<=n ; i++)
	{
		dp[i] = 1;
		for(int j = 1; j<=i; j++)
		{
			if(arr[i] > arr[j] && dp[i] == dp[j])
			{
				dp[i] = dp[j] + 1;
			}
		}
	}
	
	int max = 1;
	for(int i = 1; i<=n; i++)
	{
		if(max < dp[i])
		{
			max = dp[i];
		}
	}
	
	cout << max;
    return 0;
}
