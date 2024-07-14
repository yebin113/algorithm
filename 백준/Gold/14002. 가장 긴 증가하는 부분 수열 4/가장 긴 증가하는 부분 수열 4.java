import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans_len = 1;
        int[] arr = new int[n];
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            dp[i] = 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    ans_len = Math.max(ans_len, dp[i]);
                }

            }
        }
        System.out.println(ans_len);

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = n-1; i > -1; i--) {
            if (dp[i] == ans_len) {
                result.add(arr[i]);
                ans_len -= 1;
            }
        }
        for (int i = result.toArray().length-1; i > -1; i--) {
            System.out.print(result.get(i)+" ");
        }
//        System.out.println();

    }
}
