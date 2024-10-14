package book.집합;

import java.util.ArrayList;
import java.util.Arrays;

public class P30_간단한_유니온_파인드_알고리즘_구현하기 {
    private static int[] parent;

    private static int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }

    private static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        parent[rootY] = rootX;
    }

    private static Boolean[] solution(int k, int[][] operation) {
        parent = new int[k];
        for (int i = 0; i < k; i++) {
            parent[i] = i;
        }

        ArrayList<Boolean> answer = new ArrayList<>();
        for (int[] op : operation) {
            if (op[0] == 0) {
                union(op[1], op[2]);
            }
            else {
                if (find(op[1]) == find(op[2])) {
                    answer.add(true);
                }
                else {
                    answer.add(false);
                }
            }
        }
        return answer.toArray(new Boolean[0]);
    }
    
    public static void main(String[] args) {
        Boolean[] answer1 = solution(3, new int[][]{{0, 0, 1}, {0, 1, 2}, {1, 1, 2}});
        Boolean[] answer2 = solution(4, new int[][]{{0, 0, 1}, {1, 1, 2}, {0, 1, 2}, {1, 0, 2}});

        System.out.println(Arrays.toString(answer1));
        System.out.println(Arrays.toString(answer2));
    }
}
