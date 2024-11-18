package boj.bronze;

import java.io.*;
import java.util.Arrays;

public class 평균_1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] scores = br.readLine().split(" ");
        int sum = 0;
        int max = 0;
        for(int i = 0; i < N; i++){
            int score = Integer.parseInt(scores[i]);
            if (score > max) max = score;
            sum += score;
        }
        System.out.println("scores: " + Arrays.toString(scores));
        System.out.println(sum * 100.0 / max / N);
        System.out.println(sum / (double)max / N * 100.0);
    }
}
