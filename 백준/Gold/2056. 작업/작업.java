import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // N개의 줄
        int N = sc.nextInt();
        // dp N+1개 배열 생성
        int[] dp = new int[N+1];
        // 1~N까지
        for (int i = 1; i <= N; i++){
            // 시간을 받는다
            int hour = sc.nextInt();
            // 선행 번호의 개수
            int prev = sc.nextInt();
            // 선행 번호가 없다면 바로 저장
            if (prev == 0){
                dp[i] = hour;
            // 선행 번호가 존재한다면
            } else {
                int maxTime = 0;
                // 선행 번호가 실행된 시간중 가장 많이 걸린 시간을 계산
                for (int j = 0; j < prev; j++){
                    int prevNum = sc.nextInt();
                    maxTime = Math.max(maxTime, dp[prevNum]);
                }
                // 많이 걸린 시간에 현재 걸리는 시간을 추가
                dp[i] = maxTime + hour;
            }

        }
        int ans = 0;
        // 가장 많이 걸린 시간을 구한다
        for (int i = 1; i <= N; i++){
            ans = Math.max(ans, dp[i]);
        }
       
        System.out.println(ans);
        
    }
}