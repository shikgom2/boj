#include <iostream> 
#include <cstdlib> 
#include <algorithm> 
#include <string> 
using namespace std; 
 
int main(){
    int dp[101][101][101];  
    string str1, str2, str3; 
    cin >> str1;
    cin >> str2;
    cin >> str3;

    for(int i = 1; i <= str1.length(); i++)
    {
        for(int j = 1; j<= str2.length(); j++)
        {
            for(int k = 1; k<= str3.length(); k++)
            {
                if(str1[i-1] == str2[j-1] && str2[j-1] == str3[k-1])
                {
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
                }
                else{
                    dp[i][j][k] = max(dp[i-1][j][k] , max(dp[i][j-1][k], dp[i][j][k-1]));
                }
            }
        }
    }
    cout << dp[str1.length()][str2.length()][str3.length()] << endl;
    return 0;  
}
