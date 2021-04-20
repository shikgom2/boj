#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int i;

    cin >> i;

    for(int a = 1; a<=i; a++)
    {
        for(int b = 1; b<=a; b++)
        {
            printf("*");
        }
        printf("\n");
    }
}