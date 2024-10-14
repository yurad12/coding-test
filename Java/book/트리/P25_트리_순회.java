package book.트리;

import java.util.Arrays;

public class P25_트리_순회 {
    public static void main(String[] args) {
        String[] answer = solution(new int[]{1, 2, 3, 4, 5, 6, 7});
        System.out.println(Arrays.toString(answer));
    }

    static String[] solution(int[] nodes) {
        String[] answer = new String[3];
        answer[0] = preorder(nodes, 0).strip();
        answer[1] = inorder(nodes, 0).strip();
        answer[2] = postorder(nodes, 0).strip();

        return answer;
    }

    static String preorder(int[] nodes, int idx) {
        if (idx >= nodes.length) {
            return "";
        }
        return nodes[idx] + " " +
            preorder(nodes, idx * 2 + 1) +
            preorder(nodes, idx * 2 + 2);
    }

    static String inorder(int[] nodes, int idx) {
        if (idx >= nodes.length) {
            return "";
        }
        return inorder(nodes, idx * 2 + 1) +
            nodes[idx] + " " +
            inorder(nodes, idx * 2 + 2);
    }

    static String postorder(int[] nodes, int idx) {
        if (idx >= nodes.length) {
            return "";
        }
        return postorder(nodes, idx * 2 + 1) +
            postorder(nodes, idx * 2 + 2) +
            nodes[idx] + " ";
    }
}
