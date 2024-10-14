package book.배열;

import java.util.*;

public class P02_배열_제어하기 {
    public static void main(String[] args) {
        int[] arr = {4, 2, 2, 1, 3, 4};
        int[] answerStream = solutionStream(arr);
        int[] answerTreeSet = solutionTreeSet(arr);

        System.out.println(Arrays.toString(answerStream));
        System.out.println(Arrays.toString(answerTreeSet));
    }

    // Stream 이용
    private static int[] solutionStream(int[] arr) {
        Integer[] answer = Arrays.stream(arr).boxed().distinct().toArray(Integer[]::new);
        Arrays.sort(answer, Collections.reverseOrder());
        return Arrays.stream(answer).mapToInt(Integer::intValue).toArray();
    }

    // TreeSet 이용
    private static int[] solutionTreeSet(int[] arr) {
        TreeSet<Integer> set = new TreeSet<>(Collections.reverseOrder());
        for (int num : arr) {
            set.add(num);
        }

        int[] answer = new int[set.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = set.pollFirst();
        }
        return answer;
    }
}
