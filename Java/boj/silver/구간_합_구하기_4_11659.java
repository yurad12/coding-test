package boj.silver;

import java.io.*;
import java.util.*;

public class 구간_합_구하기_4_11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        long[] nums = new long[N+1];
        
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) { 
            nums[i] = nums[i-1] + Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(nums[b]-nums[a-1]);
        }
    }
}
