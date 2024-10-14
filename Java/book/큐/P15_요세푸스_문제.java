package book.큐;

import java.util.ArrayDeque;

public class P15_요세푸스_문제 {
    public static void main(String[] args) {
        System.out.println(solution(5, 2));
    }

    static int solution(int N, int K) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i < N + 1; i++) {
            queue.addLast(i);
        }

        while (queue.size() > 1) {
            for (int i = 0; i < K - 1; i++) {
                queue.addLast(queue.pollFirst());
            }
            queue.pollFirst();
        }
        
        return queue.pollFirst();
    }
}
