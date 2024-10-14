package book.해시;

import java.util.HashSet;

public class P18_두_개의_수로_특정값_만들기 {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {1, 2, 3, 4, 8}, 6));    
    }

    static boolean solution(int[] arr, int target) {
        HashSet<Integer> hashSet = new HashSet<>();

        for (int i : arr) {
            if (hashSet.contains(target - i)) {
                return true;
            }
            hashSet.add(i);
        }
        return false;
    }
    
}
