package book.스택;

import java.util.ArrayDeque;
import java.util.Stack;

public class P08_올바른_괄호 {
    // Stack 이용
    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack = new Stack<>();
        char[] ch = s.toCharArray();
        for (char c : ch) {
            if (c == ')' && !stack.isEmpty()) {
                stack.pop();
            }
            else {
                stack.push(c);
            }
        }
        
        if (!stack.isEmpty()) answer = false;

        return answer;
    }

    // ArrayDeque 이용
    boolean solution2(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        char[] ch = s.toCharArray();
        for (char c : ch) {
            if (c == '(') {
                stack.push(c);
            }
            else {
                if (stack.isEmpty() || stack.pop() == c)
                    return false;
            }
        }

        return stack.isEmpty();
    }
}
