package book.그래프;

import java.util.ArrayList;
import java.util.Arrays;

public class P34_깊이_우선_탐색 {
    private static ArrayList<Integer>[] adjList;
    private static boolean[] visited;
    private static ArrayList<Integer> answer;

    private static int[] solution(int[][] graph, int start, int n) {
        adjList = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int[] edge : graph) {
            adjList[edge[0]].add(edge[1]);
        }

        visited = new boolean[n + 1];
        answer = new ArrayList<>();
        dfs(start);

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    private static void dfs(int now) {
        visited[now] = true;
        answer.add(now);
        for (int next : adjList[now]) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 5}}, 1, 5)));
        System.out.println(Arrays.toString(solution(new int[][]{{1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 6}, {5, 6}}, 1, 6)));
    }
}
