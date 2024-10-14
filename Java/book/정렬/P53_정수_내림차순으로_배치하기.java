package book.정렬;

import java.util.Arrays;
import java.util.Collections;

public class P53_정수_내림차순으로_배치하기 {
    public long solution(long n) {
        String[] nums = String.valueOf(n).split("");
        Arrays.sort(nums, Collections.reverseOrder());
        
        StringBuilder sb = new StringBuilder();
        for (String s : nums) {
            sb.append(s);
        }
        
        long answer = Long.parseLong(sb.toString());
        return answer;
    }
}
