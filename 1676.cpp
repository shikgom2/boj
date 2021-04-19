#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
using namespace std;

int main(){
    int i;

    cin >> i;
    int cnt = 0;

    if(i == 0)
    {
        cout << "0" << endl;
        return 0;
    }
    for(int j = 1; j <= i; j++)
    {
        if(j%5 == 0)
        {
            cnt ++;
        }
        if(j%25 == 0){
            cnt++;
        }
        if(j%125 == 0){
            cnt ++;
        }
    }
    cout << cnt;
}