#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int i;
    int arr[11]={0,1,2,4};

    cin>>i;

    while(i--)
    {
        int k;
        cin >> k;
        for(int j = 4; j<=k; j++)
        {
            arr[j] = arr[j-1] + arr[j-2] + arr[j-3];
        }
        cout << arr[k] << endl;
    }
}