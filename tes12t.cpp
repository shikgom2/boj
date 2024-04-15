#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> a;
vector<int> w;
int N, M;

bool check(int P, set<int> &bl) {
    for (int i = 0; i < M; i++) {
        auto low = bl.lower_bound(a[i] - P / w[i]);
        auto high = bl.upper_bound(a[i] + P / w[i]);
        if (low == high) return false;
    }
    return true;
}

int main() {
    cin >> N >> M;
    set<int> bl;
    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        bl.insert(x);
    }

    for (int i = 0; i < M; i++) {
        int pos, mass;
        cin >> pos >> mass;
        a.push_back(pos);
        w.push_back(mass);
    }
    
    int left = 0, right = *bl.rbegin() - *bl.begin();

    while (left < right) {
        int mid = (left + right) / 2;
        if (check(mid, bl)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    cout << left;
}