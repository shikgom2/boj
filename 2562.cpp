#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int i = 9;
    int max = 0;
    int cnt = 0;
    int idx = 0;
    while(i--){
        cnt ++; 

        int j;

        cin >> j;

        if(j > max){
            max = j;
            idx = cnt;
        }
    }

    cout << max << endl;
    cout << idx << endl;
}