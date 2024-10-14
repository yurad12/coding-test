package book.정렬;

import java.util.ArrayList;

public class P55_가장_큰_수 {
    public String solution(int[] numbers) {
        ArrayList<String> list = new ArrayList<>();
        for (int num : numbers) {
            list.add(String.valueOf(num));
        }
        
        list.sort((o1, o2) -> {
            int a = Integer.parseInt(o1 + o2);
            int b = Integer.parseInt(o2 + o1);
            return Integer.compare(b, a);
        });
        
        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }
        
        String answer = sb.charAt(0) == '0' ? "0" : sb.toString();
        return answer;
    }
}
