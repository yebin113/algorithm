
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] party = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                party[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (party[j][k] > party[j][i] + party[i][k]) {
                        party[j][k] = party[j][i] + party[i][k];
                    }
                }
            }
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int time = sc.nextInt();
            a -= 1;
            b -= 1;
            if (party[a][b] <= time) {
                System.out.println("Enjoy other party");

            } else {
                System.out.println("Stay here");
            }

        }
    }
}
