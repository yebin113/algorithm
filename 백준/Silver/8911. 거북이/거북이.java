import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // 입력
        int T = sc.nextInt();
        sc.nextLine(); // 버퍼를 비웁니다.

        for (int t = 0; t < T; t++) {
            int leftX = 0;
            int rightX = 0;
            int topY = 0;
            int bottomY = 0;
            int[] nowLocation = {0, 0};
            // y축 상승 -> x축 상승 -> y축 하강 -> x축 하강
            int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
            int d = 0;

            String orders = sc.nextLine();

            for (int i = 0; i < orders.length(); i++) {
                char o = orders.charAt(i);
                // F: 한 눈금 앞으로
                if (o == 'F') {
                    nowLocation[0] += dir[d][0];
                    nowLocation[1] += dir[d][1];
                }
                // B: 한 눈금 뒤로
                else if (o == 'B') {
                    nowLocation[0] -= dir[d][0];
                    nowLocation[1] -= dir[d][1];
                }
                // L: 왼쪽으로 90도 회전
                else if (o == 'L') {
                    if (d == 0) {
                        d = 3;
                    } else {
                        d -= 1;
                    }
                }
                // R: 오른쪽으로 90도 회전
                else if (o == 'R') {
                    if (d == 3) {
                        d = 0;
                    } else {
                        d += 1;
                    }
                }

                leftX = Math.min(nowLocation[0], leftX);
                rightX = Math.max(nowLocation[0], rightX);
                topY = Math.max(nowLocation[1], topY);
                bottomY = Math.min(nowLocation[1], bottomY);
            }

            int area = (rightX - leftX) * (topY - bottomY);

//            System.out.printf("(%d - %d) - (%d - %d) = %d \n", rightX, leftX, topY, bottomY, area);
            System.out.println(area);
        }
    }
}
