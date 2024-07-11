import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int S = sc.nextInt();
        int E = sc.nextInt();
        int ans = 0;
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int h1 = sc.nextInt();
            int h2 = sc.nextInt();
            int k = sc.nextInt();
            graph.get(h1).add(new int[]{h2, k});
            graph.get(h2).add(new int[]{h1, k});
        }

        int start = 0;
        int end = 1000000;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            boolean check = false;
            Queue<Integer> queue = new LinkedList<>();
            boolean[] visited = new boolean[n+1];
            visited[S] = true;
            queue.add(S);
            while (!queue.isEmpty()) {
                int cur = queue.poll();
                if (cur == E) {
                    check = true;
                    break;
                }
                for (int[] neighbor : graph.get(cur)) {
                    int next = neighbor[0];
                    int weight = neighbor[1];
                    if (!visited[next] && weight >= mid) {
                        queue.add(next);
                        visited[next] = true;
                    }
                }
            }
            if (check) {
                ans = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(ans);
    }
}
