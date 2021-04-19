#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<string> v1;
    vector<string> v2;
    vector<string> v3;
    int i,j;

    cin >> i >> j;

    for(int a = 0; a<i; a++)
    {
        string tmp = "";
        cin >> tmp;
        v1.push_back(tmp);
    }

    for(int a = 0; a<j; a++)
    {
        string tmp = "";
        cin >> tmp;
        v2.push_back(tmp);
    }

    for(int a = 0; a<i; a++)
    {
        if(find(v1.begin(), v1.end(), v2[i]) != v1.end())
        {
            //element in vector
            v3.push_back(v2[i]);
        }
    }

    for(int a = v3.begin(); a != v3.end(); a++)
    {
        string tmp = "";
        cin >> tmp;
        v1.push_back(tmp);
    }


}