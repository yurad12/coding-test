package book.백트래킹;

import java.util.Arrays;

public class P44_스도쿠_퍼즐 {
    public static void main(String[] args) {
        int[][] board1 = {
                {5, 3, 0, 0, 7, 0, 0, 0, 0},
                {6, 0, 0, 1, 9, 5, 0, 0, 0},
                {0, 9, 8, 0, 0, 0, 0, 6, 0},
                {8, 0, 0, 0, 6, 0, 0, 0, 3},
                {4, 0, 0, 8, 0, 3, 0, 0, 1},
                {7, 0, 0, 0, 2, 0, 0, 0, 6},
                {0, 6, 0, 0, 0, 0, 2, 8, 0},
                {0, 0, 0, 4, 1, 9, 0, 0, 5},
                {0, 0, 0, 0, 8, 0, 0, 7, 9}
        };
        System.out.println(Arrays.deepToString(solution(board1)));

        int[][] board2 = {
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0}
        };
        System.out.println(Arrays.deepToString(solution(board2)));
    }

    private static class Block {
        int x, y;
        public Block(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static int[][] Board;

    private static boolean isValid(int num, int r, int c) {
        return !(inRow(num, r) || inCol(num, c) || inBox(num, r, c));
    } 

    private static boolean inRow(int num, int r) {
        return Arrays.stream(Board[r]).anyMatch(n -> n == num);
    }

    private static boolean inCol(int num, int c) {
        for (int i = 0; i < 9; i++) {
            if (Board[i][c] == num) return true;
        }
        return false;
    }

    private static boolean inBox(int num, int r, int c) {
        int boxR = (r / 3) * 3;
        int boxC = (c / 3) * 3;
        for (int i = boxR; i < boxR + 3; i++) {
            for (int j = boxC; j < boxC + 3; j++) {
                if (Board[i][j] == num)
                    return true;
            }
        }
        return false;
    }

    private static Block findEmptyPosition() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (Board[i][j] == 0)
                    return new Block(i, j);
            }
        }
        return null;
    }
    private static boolean find() {
        Block emptyPos = findEmptyPosition();
        if (emptyPos == null) {
            return true;
        }

        int r = emptyPos.x;
        int c = emptyPos.y;

        for (int num = 1; num <= 9; num++) {
            if (isValid(num, r, c)) {
                Board[r][c] = num;
                if (find()) {
                    return true;
                }
                Board[r][c] = 0;
            }
        }
        return false;
    }

    private static int[][] solution(int[][] board) {
        Board = board;
        find();
        return board;
    }
}
