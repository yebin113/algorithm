#include <iostream>
#include <cmath>
#include <cstdlib>  // abs() 함수 사용을 위해 추가

int main() {
    while (true) {
        int b, n;
        std::cin >> b >> n;

        // 종료 조건: b와 n이 모두 0인 경우
        if (b == 0 && n == 0) {
            break;
        }

        int ans = 0;
        int closestA = 0;
        int minDiff = abs(pow(0, n) - b); // 가장 가까운 차이를 초기화

        // A를 점차적으로 증가시키면서 A^N을 계산하고 B와의 차이를 비교
        for (int A = 0; A <= 1000000; ++A) {
            int power = pow(A, n);
            int diff = abs(power - b);

            // 차이가 더 작다면 최소 차이와 A를 업데이트
            if (diff < minDiff) {
                minDiff = diff;
                closestA = A;
            }
            // 만약 A^N이 B를 초과하는 순간, 더 이상 확인할 필요가 없으므로 종료
            if (power > b) {
                break;
            }
        }

        std::cout << closestA << std::endl;
    }

    return 0;
}
