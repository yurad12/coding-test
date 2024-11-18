package boj.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 나무_자르기_14247 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] trees = new int[n][2];
        StringTokenizer st;

        for (int i = 0; i < 2; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                trees[j][i] = Integer.parseInt(st.nextToken());
            }
        }

        Arrays.sort(trees, (o1, o2) ->
            o1[1] != o2[1] ? Integer.compare(o1[1], o2[1]) : Integer.compare(o1[0], o2[0]));

        long answer = 0;
        for (int i = 0; i < n; i++) {
            answer += (trees[i][0] + trees[i][1] * i);
        }

        System.out.println(answer);
    }
}
