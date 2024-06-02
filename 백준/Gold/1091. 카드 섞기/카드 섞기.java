import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // 입력
        int N = sc.nextInt();
        int[] p = new int[N];
        int[] s = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            s[i] = sc.nextInt();
        }
        int[] cards = new int[N];
        int[] origin = new int[N];
        for (int i = 0; i < N; i++) {
            cards[i] = i % 3;
            origin[i] = i % 3;
        }
        boolean check = true;
        int cnt = 0;
        while (!Arrays.equals(cards, p)) {
            cnt += 1;
            int[] newCards = new int[N];
            for (int i = 0; i < N; i++) {
                newCards[i] = cards[s[i]];
            }

            cards = newCards;
            if (Arrays.equals(cards, origin)) {
                System.out.println(-1);
                check = false;
                break;
            }
        }
        if (check) {
            System.out.println(cnt);
        }
    }
}
