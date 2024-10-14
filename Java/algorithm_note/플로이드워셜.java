package algorithm_note;

public class 플로이드워셜 {
    int solution(int[][] graph, int n, int x, int y) {
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    dist[i][j] = 0;
                }
                else {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int[] edge : graph) {
            dist[edge[0]][edge[1]] = edge[2];
        }
        
        for (int k = 0; k < n; k++) {
            for (int a = 0; a < n; a++) {
                for (int b = 0; b < n; b++) {
                    dist[a][b] = Math.min(dist[a][b], dist[a][k] + dist[k][b]);
                }
            }
        }

        return dist[x][y];
    }
}
