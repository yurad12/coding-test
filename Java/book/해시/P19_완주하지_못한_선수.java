package book.해시;

import java.util.HashMap;

public class P19_완주하지_못한_선수 {
    // getOrDefault 사용x
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String c : completion) {
            if (map.containsKey(c)){
                map.put(c, map.get(c) + 1);
            }
            else{
             map.put(c, 1);   
            }
        }
        
        String answer = "";
        for (String p : participant) {
            if (!map.containsKey(p) || map.get(p) <= 0) {
                answer = p;
                break;
            }
            map.put(p, map.get(p) - 1);
        }
        
        return answer;
    }

    // getOrDefault 사용o
    public String solution2(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String c : completion) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        for (String p : participant) {
            if (map.getOrDefault(p, 0) == 0) {
                return p;
            }
            map.put(p, map.get(p) - 1);
        }
        return null;
    }
}
