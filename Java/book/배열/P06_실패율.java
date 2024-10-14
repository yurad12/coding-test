package book.배열;

import java.util.HashMap;

public class P06_실패율 {
    public int[] solution(int N, int[] stages) {
        int[] count = new int[N+2];
        for (int s : stages) {
            count[s]++;
        }
        
        HashMap<Integer, Double> failRate = new HashMap<>();
        double total = stages.length;
        for (int i = 1; i <= N; i++) {
            if (count[i] == 0) {
                failRate.put(i, 0.);
            }
            else {
                failRate.put(i, count[i] / total);
                total -= count[i];
            }
        }
        
        return failRate.entrySet().stream()
            .sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue()))
            .mapToInt(HashMap.Entry::getKey).toArray();
    }
}
