package book.배열;

import java.util.ArrayList;
import java.util.Arrays;

public class P04_모의고사 {
        public int[] solution(int[] answers) {
        int[][] pattern = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5}
        };
        
        int[] count = new int[3];
        for (int i = 0; i < pattern.length; i++) {
            for (int j = 0; j < answers.length; j++) {
                if (answers[j] == pattern[i][j % pattern[i].length]) {
                    count[i]++;
                }
            }
        }
        
        int maxCount = Arrays.stream(count).max().getAsInt();
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (count[i] == maxCount) {
                answer.add(i+1);
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
