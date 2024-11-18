package boj.silver;

import java.io.*;
import java.util.*;

public class 단어_정렬_1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashSet<String> wordSet = new HashSet<>();
        for (int i = 0; i < N; i++) {
            wordSet.add(br.readLine());
        }

        ArrayList<String> words = new ArrayList<>(wordSet);
        Collections.sort(words, 
            (o1, o2) -> o1.length() != o2.length() ? 
            Integer.compare(o1.length(), o2.length()) : o1.compareTo(o2));
        
        for (String word : words) {
            System.out.println(word);
        }
    }
}
