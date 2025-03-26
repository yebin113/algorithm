/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
int main()
{
    const int rows = 5;
    
    std::vector<std::string> arr(rows) ;
    for (int i=0;i<rows;i++){
        std::getline(std::cin,arr[i]);
    }
    
    int maxLength = 0;
    for (const auto& str : arr) {
        if (str.length() > maxLength) {
            maxLength = str.length();
        }
    }
    
    for (int i = 0; i < maxLength; i++) {
        for (int j = 0; j < rows; j++) {
            if (i < arr[j].length()) { 
                std::cout << arr[j][i];
            }
        }
    }

    return 0;
}