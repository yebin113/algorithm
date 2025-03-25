/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
int main()
{
    int n;
    std::cin >> n;
    
    
    // 배열 선언
    std::vector<int> dp(n+1) ;
    dp[1] = 1;
    
    for (int i= 2; i <n+1; i++){
        dp[i] = dp[i-1] + dp[i-2];
    }
    std::cout << dp[n];
    

    return 0;
}