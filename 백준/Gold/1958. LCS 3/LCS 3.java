import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // 입력
        String a = "0"+sc.nextLine();
        String b = "0"+sc.nextLine();
        String c = "0"+sc.nextLine();

        int [][][]dp = new int[a.length()][b.length()][c.length()];

        for(int i = 1; i < a.length(); i++){
            for(int j = 1; j < b.length(); j++){
                for(int k = 1; k < c.length(); k++){
                    if (a.charAt(i) == b.charAt(j) && b.charAt(j)== c.charAt(k)){
                        dp[i][j][k] = dp[i-1][j-1][k-1]+1;
                    } else {
                        dp[i][j][k] = Math.max(Math.max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1]);

                    }
                }
            }
        }
        System.out.println(dp[a.length()-1][b.length()-1][c.length()-1]);
    }
}
