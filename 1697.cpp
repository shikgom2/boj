#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

const int MAX = 200000;
int dist[MAX+1];

int main() {
    int n, m;
    cin >> n >> m;
    memset(dist, -1, sizeof(dist)); 
    dist[n] = 0;
    queue<int> q;
    q.push(n);
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        if (now*2 < MAX) {
            if (dist[now*2] == -1) {
                q.push(now*2);
                dist[now*2] = dist[now] + 1;
            }
        }
        if (now+1 < MAX) {
            if (dist[now+1] == -1) {
                q.push(now+1);
                dist[now+1] = dist[now] + 1;
            }
        }
        if (now-1 >= 0) {
            if (dist[now-1] == -1) {
                q.push(now-1);
                dist[now-1] = dist[now] + 1;
            }
        }
    }
    cout << dist[m] << '\n';
    return 0;
}