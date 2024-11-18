package boj.gold;

import java.io.*;
import java.util.*;

public class 나머지_합_10986 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        long[] nums = new long[N];
        long[] count = new long[M];
        
        st = new StringTokenizer(br.readLine());
        nums[0] = Integer.parseInt(st.nextToken());
        for (int i = 1; i < N; i++) {
            nums[i] = nums[i-1] + Integer.parseInt(st.nextToken());
        }

        long answer = 0;
        for (int i = 0; i < N; i++) {
            int r = (int) (nums[i] % M);
            if (r == 0) answer ++;
            count[r] ++;
        }

        for (int i = 0; i < M; i++) {
            if (count[i] > 1) {
                answer += (count[i] * (count[i] - 1) / 2);
            }
        }
        
        System.out.println(answer);
    }    
}
