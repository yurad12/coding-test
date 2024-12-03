package boj.silver;

import java.util.Scanner;

public class 달팽이_1913 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int N2 = sc.nextInt();

        int[][] snail = new int[N][N];
        int startRow = 0, endRow = N-1;
        int startCol = 0, endCol = N-1;
        int num = N * N;
        int x = -1, y = -1;

        while (startRow <= endRow && startCol <= endCol) {
            for (int i = startRow; i <= endRow; i++) {
                snail[i][startCol] = num;
                if (num == N2) {
                    x = i;
                    y = startCol;
                }
                num--;
            }
            startCol++;

            for (int j = startCol; j <= endCol; j++) {
                snail[endRow][j] = num;
                if (num == N2) {
                    x = endRow;
                    y = j;
                }
                num--;
            }
            endRow--;

            for (int i = endRow; i >= startRow; i--) {
                snail[i][endCol] = num;
                if (num == N2) {
                    x = i;
                    y = endCol;
                }
                num--;
            }
            endCol--;

            for (int j = endCol; j >= startCol; j--) {
                snail[startRow][j] = num;
                if (num == N2) {
                    x = startRow;
                    y = j;
                }
                num--;
            }
            startRow++;
        }

        StringBuilder sb;
        for (int i = 0; i < N; i++) {
            sb = new StringBuilder();
            for (int j = 0; j < N; j++) {
                sb.append(snail[i][j]).append(" ");
            }
            System.out.println(sb.toString().strip());
        }

        sb = new StringBuilder();
        sb.append(x+1).append(" ").append(y+1);
        System.out.println(sb.toString());

        sc.close();
    }
}
