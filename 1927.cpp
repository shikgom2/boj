#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
#include <stdio.h>

using namespace std;


int main() {
	int n;
	priority_queue<int, vector<int>, less<int>> q;
	cin >> n;

	while(n--){
		int m;
		
		cin >> m;
		
		if(m == 0)
		{
			if(q.empty())
			{
				cout << "0";
			}
			else{
				cout << q.top();
				q.pop();
			}
		}
		else{
			q.push(m);
		}
	}
    return 0;
}
