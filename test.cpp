#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    int arr[1000000];

    cin >> tc;

    for (int i = 0; i < tc; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + tc, greater<int>());

    for (int i = 0; i < tc; i++) {
        cout << arr[i] << '\n';
    }

    return 0;
}