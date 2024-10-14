package book.정렬;

import java.util.Arrays;

public class P54_K번째수 {
    // my solution
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int c = 0; c < commands.length; c++) {
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];
            
            int n = j - i + 1;
            int[] sliced = new int[n];
            int idx = 0;
            for (int a = i - 1; a < j; a++) {
                sliced[idx++] = array[a];
            }
            Arrays.sort(sliced);
            answer[c] = sliced[k-1];
        }
        return answer;
    }

    // book solution
    public int[] solution2(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int c = 0; c < commands.length; c++) {
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];

            int[] sliced = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(sliced);
            answer[c] = sliced[k-1];
        }
        return answer;
    }
}
