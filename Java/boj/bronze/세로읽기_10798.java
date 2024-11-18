package boj.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 세로읽기_10798 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] words = new char[5][15];

        for (int i = 0; i < 5; i++) {
            char[] word = br.readLine().toCharArray();
            for (int j = 0; j < word.length; j++) {
                words[i][j] = word[j];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < 15; j++) {
            for (int i = 0; i < 5; i++) {
                if (words[i][j] != 0) {
                    sb.append(words[i][j]);
                }
            }
        }

        System.out.println(sb.toString());
    }
}
