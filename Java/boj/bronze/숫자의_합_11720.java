package boj.bronze;

import java.io.*;

public class 숫자의_합_11720 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String sNum = br.readLine();
        int answer = 0;
        for (int i = 0; i < N; i++){
            answer += sNum.charAt(i) - '0';
        }

        System.out.println(answer);
    }
}
