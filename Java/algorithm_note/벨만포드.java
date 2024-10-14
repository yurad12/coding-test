package algorithm_note;

import java.util.Arrays;

public class 벨만포드 {
    private static boolean solution(int[][] graph, int start, int n) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);

        dist[start] = 0;
        for (int v = 0; v < n; v++) {
            for (int e = 0; e < graph.length; e++) {
                int[] edge = graph[e];
                if (dist[edge[0]] != Integer.MAX_VALUE && dist[edge[1]] > dist[edge[0]] + edge[2]) {
                    dist[edge[1]] = dist[edge[0]] + edge[2];
                    if (v == n - 1) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
