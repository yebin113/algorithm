#include <iostream>

int main(int argc, char **argv){
    // 변수 초기화
    int T, a, b, tmp = 1;
    // 테스트 케이스 입력 받기
    scanf("%d",&T);
    // 테스트 케이스 만큼 반복
    for(int i=0; i<T; i++){
        // a,b 입력받음
        scanf("%d %d",&a,&b); 
        // 나머지 출력
        for(int j=0; j<b; j++){
            tmp = (tmp * a) % 10;
        }
        if(tmp == 0){
            printf("10\n"); 
        } else {
            printf("%d\n",tmp);
        }
        // 초기화
        tmp = 1;
    }

    return 0;
}