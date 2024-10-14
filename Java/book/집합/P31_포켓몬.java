package book.집합;

import java.util.HashSet;

public class P31_포켓몬 {
    public int solution(int[] nums) {
        HashSet<Integer> pokemon = new HashSet<>();
        for (int n : nums) {
            pokemon.add(n);
        }
        int answer = pokemon.size();
        if (nums.length / 2 < answer) {
            answer = nums.length / 2;
        }
        return answer;
    }
}
