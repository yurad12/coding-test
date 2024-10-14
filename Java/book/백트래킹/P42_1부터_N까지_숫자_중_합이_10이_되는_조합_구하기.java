package book.백트래킹;

import java.util.ArrayList;

public class P42_1부터_N까지_숫자_중_합이_10이_되는_조합_구하기 {
    private static ArrayList<ArrayList<Integer>> answer;
    private static int n;

    private static void backtrack(ArrayList<Integer> nums, int x, int sum) {
        if (sum == 10) {
            answer.add(nums);
            return;
        }

        for (int i = x; i <= n; i++) {
            if (sum + i <= 10) {
                ArrayList<Integer> newNums = new ArrayList<>(nums);
                newNums.add(i);
                backtrack(newNums, i + 1, sum + i);
            }
        }
    }

    private static ArrayList<ArrayList<Integer>> solution(int N) {
        answer = new ArrayList<>();
        n = N;
        backtrack(new ArrayList<>(), 1, 0);

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(5));
        System.out.println(solution(2));
        System.out.println(solution(7));
    }
}