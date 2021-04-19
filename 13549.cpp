#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
	
	queue<pair<long long, int>> q;
	
	long long a;
	long long b;
	
	
	cin >> a >> b;
	
	q.push({a,0});
	
	while(!q.empty())
	{
		pair<long long, int> tmp = q.front();
		//cout << tmp.first << endl;
		q.pop();
		
		if(tmp.first == b)
		{
			cout << tmp.second + 1 << endl;
			return 0;
		}
		
		if(tmp.first * 2 <= b)
		{
			q.push({tmp.first * 2 , tmp.second});
		}
		if(tmp.first + 1 <= b)
		{
			q.push({tmp.first + 1, tmp.second + 1});
		}
        if(tmp.first - 1 == b)
        {
            q.push({tmp.first-1 , tmp.second + 1});
        }
	}
    return 0;
}
