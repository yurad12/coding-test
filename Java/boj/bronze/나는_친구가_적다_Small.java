package boj.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 나는_친구가_적다_Small {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String target = br.readLine();

        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) {
                sb.append(c);
            }
        }

        if (sb.toString().contains(target)) {
            System.out.println(1);
        }
        else {
            System.out.println(0);
        }
    }
}