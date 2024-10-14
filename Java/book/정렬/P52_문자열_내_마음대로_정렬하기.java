package book.정렬;

import java.util.Arrays;

public class P52_문자열_내_마음대로_정렬하기 {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (o1, o2) -> 
                   o1.charAt(n) == o2.charAt(n) ?
                   o1.compareTo(o2) :
                    Character.compare(o1.charAt(n), o2.charAt(n)));
        return strings;
    }
}
