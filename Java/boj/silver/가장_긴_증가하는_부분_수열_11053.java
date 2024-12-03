package boj.silver;

import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class 가장_긴_증가하는_부분_수열_11053 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N];
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i] > A[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        System.out.println(IntStream.of(dp).max().getAsInt());
    }
}
