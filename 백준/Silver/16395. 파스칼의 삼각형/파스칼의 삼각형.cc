/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
int main()
{
    // 입력
    int n;
    int k;
    std::cin >> n;
    std::cin >> k;
    
    // 배열 선언
    std::vector<std::vector<int>> dp(n) ;
    for (int i= 0; i <n; i++){
        dp[i] = std::vector<int>(i+1,1);
    }
    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < i ; j ++ ){
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
        }
    }
    
    std::cout << dp[n-1][k-1];

    return 0;
}