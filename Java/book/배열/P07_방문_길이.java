package book.배열;

import java.util.HashMap;
import java.util.HashSet;

public class P07_방문_길이 {
    public int solution(String dirs) {
        HashMap<Character, int[]> d = new HashMap<>();
        d.put('U', new int[]{0, 1});
        d.put('D', new int[]{0, -1});
        d.put('R', new int[]{1, 0});
        d.put('L', new int[]{-1, 0});
        
        int x = 0;
        int y = 0;
        HashSet<String> visited = new HashSet<>();
        for (int i = 0; i < dirs.length(); i++) {
            char c = dirs.charAt(i);
            int nx = x + d.get(c)[0];
            int ny = y + d.get(c)[1];
            
            if (nx < -5 || nx > 5 || ny < -5 || ny > 5) {
                continue;
            }
            
            visited.add(x + " " + y + " " + nx + " " + ny);
            visited.add(nx + " " + ny + " " + x + " " + y);
            x = nx;
            y = ny;
        }
        int answer = visited.size() / 2;
    return answer;
    }
}
