#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int i;
    scanf("%d", &i);

    priority_queue<int> pq;

    while(i--)
    {
        int j;
        scanf("%d", &j);

        if(j == 0)
        {
            if(pq.empty())
            {
                printf("0\n");
            }
            else{
                printf("%d\n", pq.top());
                pq.pop();
            }
        }
        else{
            pq.push(j);
        }
    }
}