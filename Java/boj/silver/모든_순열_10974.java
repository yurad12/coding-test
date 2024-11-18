package boj.silver;

import java.util.Scanner;
import java.util.stream.IntStream;

public class 모든_순열_10974 {
    static int N;
    static int[] arr;

    private static void permutation(boolean[] visited, int[] answer, int depth) {
        if (depth == N) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < N; i++) {
                sb.append(answer[i]).append(" ");
            }
            System.out.println(sb.toString().strip());
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i])
                continue;

            visited[i] = true;
            answer[depth] = arr[i];
            permutation(visited, answer, depth + 1);
            visited[i] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = IntStream.range(1, N+1).toArray();
        int[] answer = new int[N];
        boolean[] visited = new boolean[N];
        permutation(visited, answer, 0);

        sc.close();
    }
}
