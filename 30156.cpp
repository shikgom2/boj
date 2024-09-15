#include<bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        string s;
        cin >> s;
        int ans1 = 0;
        int ans2 = 0;

        for(int i = 0 ; i< s.length(); i++){
            if(s[i] == 'a'){
                ans1 ++;
            }
            else{
                ans2 ++;
            }
        }
        cout << (ans1 >= ans2? ans2 : ans1) << endl;
    }
    return 0;
}