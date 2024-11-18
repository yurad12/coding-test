package boj.silver;

import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class ROT13_4446 {
    static final String vowels = "aiyeou";
    static final String consonants = "bkxznhdcwgpvjqtsrlmf";

    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        HashMap<Character, Character> vowelMap = new HashMap<>();
        HashMap<Character, Character> consonantMap = new HashMap<>();

        for (int i = 0; i < vowels.length(); i++) {
            char now = vowels.charAt(i);
            char next = vowels.charAt((i+3) % vowels.length());
            vowelMap.put(now, next);
            vowelMap.put(Character.toUpperCase(now), Character.toUpperCase(next));
        }

        for (int i = 0; i < consonants.length(); i++) {
            char now = consonants.charAt(i);
            char next = consonants.charAt((i+10) % consonants.length());
            consonantMap.put(now, next);
            consonantMap.put(Character.toUpperCase(now), Character.toUpperCase(next));
        }

        while (sc.hasNextLine()) { // (s = br.readLine()) != null
            String s = sc.nextLine();
            StringBuilder sb = new StringBuilder();

            for (char c : s.toCharArray()) {
                if (vowelMap.containsKey(c)) {
                    sb.append(vowelMap.get(c));
                }
                else if (consonantMap.containsKey(c)) {
                    sb.append(consonantMap.get(c));
                }
                else {
                    sb.append(c);
                }
            }

            System.out.println(sb.toString());
        }

        sc.close();
    }
}
