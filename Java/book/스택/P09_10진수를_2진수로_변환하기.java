package book.스택;

import java.util.ArrayDeque;

public class P09_10진수를_2진수로_변환하기 {
    public static void main(String[] args) {
        System.out.println(solution(10));
        System.out.println(solution(27));
        System.out.println(solution(12345));
    }

    static String solution(int decimal) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        while (decimal > 0) {
            stack.push(decimal % 2);
            decimal /= 2;
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        return sb.toString();
    }
}
