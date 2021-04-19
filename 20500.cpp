#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
using namespace std;

int dp[61][61][61]; 
	
int solve(int a, int b, int c)
{
	if(a < 0)
	{
		a = 0;
	}
	if(b < 0)
	{
		b = 0;
	} 
	if(c < 0)
	{
		c = 0;
	} 
	
	if(a == 0 && b == 0 && c == 0)
	{
		return 0;
	}
	
	int& tmp = dp[a][b][c];
	if(tmp != -1)
	{
		return tmp;
	}
	
	tmp = 999999999;
	
	tmp = min(tmp, solve(a-9, b-3, c-1) + 1);
	tmp = min(tmp, solve(a-9, b-1, c-3) + 1);
	tmp = min(tmp, solve(a-3, b-1, c-9) + 1);
	tmp = min(tmp, solve(a-3, b-9, c-1) + 1);
	tmp = min(tmp, solve(a-1, b-3, c-9) + 1);
	tmp = min(tmp, solve(a-1, b-9, c-3) + 1);	
	
	return tmp;
}

int main() {
	
	int n;
	int val[3] = {0,0,0};
	
	cin >> n;
	
	for(int i = 0; i<n; ++i	)
	{
		cin >> val[i];
	}
	
	memset(dp, -1, sizeof(dp));
	
	cout << solve(val[0], val[1], val[2]);
	
    return 0;
}
