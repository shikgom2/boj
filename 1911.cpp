#include <bits/stdc++.h> 
using namespace std;

 
int main() {
    cin.tie(0); 
    ios_base::sync_with_stdio(0);
    cout.tie(0);
    
    int n, l;
    vector<pair<int, int>> li;

    cin >> n >> l;
    for (int i = 0; i < n; ++i) {
        int s, e;
        cin >> s >> e;
        li.push_back({s, e});
    }
    
    sort(li.begin(), li.end());
    
    int ans = 0;
    int cov = 0;

    for (auto &p : li) {
        int start = p.first, end = p.second;
        
        if (cov >= end)
            continue;
        
        if (cov < start)
            cov = start;
        
        int gap = end - cov;
        int b = (gap + l - 1) / l;
        ans += b;
        cov += b * l;
    }
    
    cout << ans;
    
    return 0;
}
