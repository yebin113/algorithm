/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <string>

int main()
{
    int n;
    std::cin >> n;
    bool flag = false;
    for(int i=1;i<n+1;i++){
        int addedNum = i;
        int number = i;
        while (number != 0){
            int num = number %10;
            number = number/10;
            addedNum += num;
        }
        if (addedNum == n){
            flag = true;
            std::cout << i << std::endl;
            break;
        }
        
    }
    if (flag == false){
        std::cout << 0 << std::endl;
    }

    return 0;
}