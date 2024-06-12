import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static int[] visited;
    private static int[] depth;
    private static int[] parent;
    private static List<Integer>[] graph;
    private static int n;
    private static int answer;

    // 자바는 제네릭 배열 생성을 지원하지 않기 때문에, 이 경고를 무시하고 배열을 초기화하기 위한 것이라는데 뭔지 모르겠다
    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new ArrayList[n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // 배열 초기화
        parent = new int[n + 1];
        visited = new int[n + 1];
        depth = new int[n + 1];

        // n-1 줄로 이루어진 간선 정보
        for (int i = 1; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            graph[b].add(a);
        }
        //  루트 노드는 1로 초기화해서 depth를 저장해줌
        findDepth(1, 0);
        int m = sc.nextInt();
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            solve(a, b);
            System.out.println(answer);
        }

        sc.close();
    }

    // 깊이 저장 -> dfs 구조
    private static void findDepth(int a, int step) {
        visited[a] = 1;
        depth[a] = step;
        for (int nextA : graph[a]) {
            if (visited[nextA] == 0) {
                parent[nextA] = a;
                findDepth(nextA, step + 1);
            }
        }
    }

    // 같은 부모 찾기
    private static void solve(int a, int b) {
        // 깊이가 다른경우 깊이가 더 깊은 쪽을 부모로 올림
        while (depth[a] != depth[b]) {
            if (depth[a] > depth[b]) {
                a = parent[a];
            } else {
                b = parent[b];
            }
        }

        // 깊이가 같은 경우 동시에 부모로 올라감
        while (a != b) {
            a = parent[a];
            b = parent[b];
        }
        //  답을 적용해준다
        answer = a;
    }
}
