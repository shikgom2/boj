#include <iostream>
#include <vector>

#define MAX_SIZE 2002
#define NOT_YET_MEMOIZED 0
using namespace std;

int arr[MAX_SIZE][MAX_SIZE] = {0, };
int dp[MAX_SIZE][MAX_SIZE] = {0, };

int main(){
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            scanf("%d", &arr[i][j]);
            dp[i][j] = NOT_YET_MEMOIZED;
        }
    }

    for(int i = 1; i <= n; i++)
    {
        for(int j = n; j >= 0; j--)
        {
            if(i == 1 && j == n)
            {
                dp[i][j] = arr[i][j];
            }

            if(dp[i][j-1] == NOT_YET_MEMOIZED)  //left
            {
                dp[i][j-1] = dp[i][j] + arr[i][j-1];
            }
            else{
                dp[i][j-1] = min(dp[i][j-1], dp[i][j] + arr[i][j-1]);
            }

            if(dp[i+1][j-1] == NOT_YET_MEMOIZED)    //left down
            {
                dp[i+1][j-1] = dp[i][j] + arr[i+1][j-1];
            }
            else{
                dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j] + arr[i+1][j-1]);
            }

            if(dp[i+1][j] == NOT_YET_MEMOIZED)  // down
            {
                dp[i+1][j] = dp[i][j] + arr[i+1][j];
            }
            else{
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + arr[i+1][j]);
            }
        }
    }
    cout << dp[n][0] << endl;

    return 0;
}