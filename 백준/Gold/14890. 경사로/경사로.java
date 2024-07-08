import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int l = sc.nextInt();
        int cnt = 0;
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < n; i++) {
            List<Integer> verticalLine = new ArrayList<>();
            List<Integer> horizontalLine = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                verticalLine.add(arr[i][j]);
                horizontalLine.add(arr[j][i]);
            }

            if (check(verticalLine, l)) {
                cnt += 1;
            }
            if (check(horizontalLine, l)) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }

    private static boolean check(List<Integer> arr, int l) {
        int n = arr.size();
        int prev = arr.get(0);
        int curGround = 1;
        boolean isSettled = false;

        for (int i = 1; i < n; i++) {
            if (i < n - 1 && arr.get(i - 1).equals(arr.get(i + 1)) && arr.get(i - 1) > arr.get(i)) {
                return false;
            }

            if (Math.abs(arr.get(i) - prev) > 1) {
                return false;
            } else if (arr.get(i).equals(prev)) {
                curGround += 1;
                if (isSettled && curGround >= l) {
                    isSettled = false;
                    curGround = 0;
                }
            } else if (arr.get(i) > prev) {
                if (!isSettled && curGround >= l) {
                    isSettled = false;
                    curGround = 1;
                } else {
                    return false;
                }
                prev = arr.get(i);
            } else if (arr.get(i) < prev) {
                if (isSettled) {
                    return false;
                }
                curGround = 1;
                prev = arr.get(i);
                if (l == 1) {
                    continue;
                }
                isSettled = true;
            }
        }
        return !isSettled;
    }
}
