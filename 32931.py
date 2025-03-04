#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
vector<int> a;
vector<int> seg;

void build(int idx, int l, int r) {
    if(l == r) {
        seg[idx] = a[l];
        return;
    }
    int mid = (l + r) / 2;
    build(idx*2, l, mid);
    build(idx*2+1, mid+1, r);
    seg[idx] = max(seg[idx*2], seg[idx*2+1]);
}

int findRightmost(int idx, int l, int r, int ql, int qr, int X) {
    if(r < ql || l > qr) return -1;
    if(ql <= l && r <= qr) {
        if(seg[idx] < X) return -1;
        if(l == r) return l;
    }
    int mid = (l + r) / 2;
    int res = findRightmost(idx*2+1, mid+1, r, ql, qr, X);
    if(res != -1) return res;
    return findRightmost(idx*2, l, mid, ql, qr, X);
}

int findLeftmost(int idx, int l, int r, int ql, int qr, int X) {
    if(r < ql || l > qr) return -1;
    if(ql <= l && r <= qr) {
        if(seg[idx] < X) return -1;
        if(l == r) return l;
    }
    int mid = (l + r) / 2;
    int res = findLeftmost(idx*2, l, mid, ql, qr, X);
    if(res != -1) return res;
    return findLeftmost(idx*2+1, mid+1, r, ql, qr, X);
}

bool canDo(int p, int tar) {
    for (int i = 0; i < n; i++) {
        if(a[i] < p) continue;  // 중심 후보 조건
        // 왼쪽 그리디 선택
        int left_count = 0;
        int pos = i - 1;
        int need = p - 1;
        while(pos >= 0) {
            int j = findRightmost(1, 0, n-1, 0, pos, need);
            if(j == -1) break;
            left_count++;
            pos = j - 1;
            need = p - (left_count + 1);
        }
        // 오른쪽 그리디 선택
        int right_count = 0;
        pos = i + 1;
        need = p - 1;
        while(pos < n) {
            int j = findLeftmost(1, 0, n-1, pos, n-1, need);
            if(j == -1) break;
            right_count++;
            pos = j + 1;
            need = p - (right_count + 1);
        }
        if(left_count + 1 + right_count >= tar)
            return true;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--){
        cin >> n >> k;
        a.resize(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        int tar = n - k;
        int mx = *max_element(a.begin(), a.end());
        
        seg.assign(4*n, 0);
        build(1, 0, n-1);
        
        int lo = 1, hi = mx + 1, ans = 1;
        while(lo < hi){
            int mid = (lo + hi) / 2;
            if(canDo(mid, tar)){
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
