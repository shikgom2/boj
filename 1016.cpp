#include <cstdio>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;
bool IsChecked[1000001];
bool IsSquare[1000001];

int main() 
{
    long long min, max;
    scanf("%lld %lld", &min, &max);

    long long ans = max - min + 1;
    for (long long i = 2; i * i <= max; ++i)
    {
        if (IsChecked[i])
            continue;
        for (long long j = i; j * j <= max; j += i)
            IsChecked[j] = true;

        long long square = i * i;
        for (long long j = ((min - 1) / square + 1) * square; j <= max; j += square)
        {
            if (IsSquare[j - min] == false)
            {
                IsSquare[j - min] = true;
                --ans;
            }

        }

    }
    printf("%lld", ans);
}
