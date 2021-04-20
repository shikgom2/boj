#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int i,j;

    scanf("%d %d", &i,&j);

    if(i>j){
        printf(">");
    }
    else if(i<j)
    {
        printf("<");
    }
    else{
        printf("==");
    }
}