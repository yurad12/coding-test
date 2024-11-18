package boj.bronze;

import java.io.*;
import java.util.*;

public class 알파벳_찾기_10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        solution1(s);
        solution2(s);
    }

    static void solution1(String s) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = (int) 'a'; i <= (int) 'z'; i++) {
            map.put(i, -1);
        }

        for (int i = 0; i < s.length(); i++){
            int n = (int) s.charAt(i);
            if (map.get(n) == -1) {
                map.put(n, i);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int v : map.values()) {
            sb.append(v).append(" ");
        }

        System.out.println(sb.toString().strip());
    }

    static void solution2(String s) {
        int[] positions = new int[26];
        Arrays.fill(positions, -1);

        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (positions[idx] == -1) {
                positions[idx] = i;
            }
        }

        for (int i = 0; i < positions.length; i++) {
            System.out.print(positions[i]);
            if (i < positions.length - 1) {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
}
