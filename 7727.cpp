#include<bits/stdc++.h>
using namespace std;

vector<int> lcs(const std::string& A, const std::string& B) {
    int n = B.size();
    std::vector<int> curr(n + 1, 0);

    for (char a : A) {
        std::vector<int> prev = curr;
        for (int j = 1; j <= n; ++j) {
            if (a == B[j - 1])
                curr[j] = prev[j - 1] + 1;
            else
                curr[j] = std::max(curr[j - 1], prev[j]);
        }
    }
    return curr;
}

string Hirschberg(const string& A, const string& B) {
    int m = A.size();
    int n = B.size();

    if (m == 0) {
        return "";
    } else if (m == 1) {
        // A의 길이가 1인 경우, B에서 해당 문자가 있는지 확인
        if (B.find(A[0]) != std::string::npos)
            return A;
        else
            return "";
    } else {
        int mid = m / 2;

        // A의 전반부와 B의 LCS 길이 계산
        std::vector<int> L1 = lcs(A.substr(0, mid), B);

        // A의 후반부와 B의 역순에 대한 LCS 길이 계산
        string A_rev = string(A.rbegin(), A.rend());
        string B_rev = string(B.rbegin(), B.rend());
        vector<int> L2 = lcs(A_rev.substr(0, m - mid), B_rev);

        // 분할 지점 찾기
        int k = 0;
        int max = 0;
        for (int j = 0; j <= n; ++j) {
            int l1 = L1[j];
            int l2 = L2[n - j];
            if (l1 + l2 > max) {
                max = l1 + l2;
                k = j;
            }
        }

        string left = Hirschberg(A.substr(0, mid), B.substr(0, k));
        string right = Hirschberg(A.substr(mid), B.substr(k));

        return left + right;
    }
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n,m;
    cin>>n>>m;
    string A, B;
    cin >> A;
    cin >> B;

    string ans = Hirschberg(A, B);

    cout << ans.length() << endl;
    cout << ans << std::endl;

    return 0;
}
