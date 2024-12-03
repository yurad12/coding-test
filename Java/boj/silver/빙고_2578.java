package boj.silver;

import java.io.*;
import java.util.*;

public class 빙고_2578 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[5][5];
        StringTokenizer st;
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] numbers = new int[25];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                numbers[i * 5 + j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 0;
        boolean[][] called = new boolean[5][5];

        for (int idx = 0; idx < 25; idx++) {
            int num = numbers[idx];

            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (board[i][j] == num) {
                        called[i][j] = true;
                    }
                }
            }

            if (checkBingo(called) >= 3) {
                answer = idx + 1;
                break;
            }
        }

        System.out.println(answer);

        br.close();
    }

    private static int checkBingo(boolean[][] called) {
        int count = 0;

        for (int i = 0; i < 5; i++) {
            boolean bingo = true;
            for (int j = 0; j < 5; j++) {
                if (!called[i][j]) {
                    bingo = false;
                    break;
                }
            }
            if (bingo)
                count++;
        }

        for (int j = 0; j < 5; j++) {
            boolean bingo = true;
            for (int i = 0; i < 5; i++) {
                if (!called[i][j]) {
                    bingo = false;
                    break;
                }
            }
            if (bingo)
                count++;
        }

        boolean bingo = true;
        for (int i = 0; i < 5; i++) {
            if (!called[i][i]) {
                bingo = false;
                break;
            }
        }
        if (bingo)
            count++;
        
        bingo = true;
        for (int i = 0; i < 5; i++) {
            if (!called[i][4-i]) {
                bingo = false;
                break;
            }
        }
        if (bingo)
            count++;

        return count;
    }
}
