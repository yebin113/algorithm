/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <algorithm>
int main()
{
    std::vector<int> arr(3);
    
    // 입력 받기
    for (int i = 0; i < 3; i++) {
        std::cin >> arr[i];
    }
    
    // 정렬
    std::sort(arr.begin(), arr.end());

    // 가장 큰 값과 두 번째, 세 번째 값 할당
    int maxNum = arr[2];
    int secondNum = arr[1];
    int minNum = arr[0];
    
    if (maxNum >= secondNum + minNum) {
        std::cout << 2*(secondNum + minNum) - 1 << std::endl;
    } else {
        std::cout << maxNum+secondNum+minNum << std::endl;
    }
    

    return 0;
}