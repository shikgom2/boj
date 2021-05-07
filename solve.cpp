#include <iostream>
#include <vector>

#define MAX_SIZE 2001
#define NOT_YET_MEMOIZED 0
using namespace std;

int arr[MAX_SIZE][MAX_SIZE] = {0, };
int dp[MAX_SIZE][MAX_SIZE] = {0, };

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &arr[i][j]);
            dp[i][j] = NOT_YET_MEMOIZED;
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = n-1; j >= 0; j--)
        {
            if(i == 0 && j == n-1)
            {
                dp[i][j] = arr[i][j];
            }

            if(dp[i][j-1] == NOT_YET_MEMOIZED)
            {
                dp[i][j-1] = dp[i][j] + arr[i][j-1];
            }
            else{
                dp[i][j-1] = min(dp[i][j-1], dp[i][j] + arr[i][j-1]);
            }

            if(dp[i+1][j-1] == NOT_YET_MEMOIZED)
            {
                dp[i+1][j-1] = dp[i][j] + arr[i+1][j-1];
            }
            else{
                dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j] + arr[i+1][j-1]);
            }

            if(dp[i+1][j] == NOT_YET_MEMOIZED)
            {
                dp[i+1][j] = dp[i][j] + arr[i+1][j];
            }
            else{
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + arr[i+1][j]);
            }
        }
    }
    cout << dp[n-1][0] << endl;

    return 0;
}