package boj.bronze;

import java.io.*;

public class 암호_1718 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        char[] plain = bf.readLine().toCharArray();
        char[] key = bf.readLine().toCharArray();

        solution(plain, key);
    }

    static void solution(char[] plain, char[] key) {
        int n = key.length;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < plain.length; i++) {
            if (plain[i] == ' ') {
                sb.append(" ");
                continue;
            }
            int num = ((plain[i] - 'a') - (key[i % n] - 'a') + 25) % 26;
            sb.append((char) (num + 'a'));
        }
        System.out.println(sb.toString());
    }
}