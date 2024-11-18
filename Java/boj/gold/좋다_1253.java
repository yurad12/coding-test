package boj.gold;

import java.io.*;
import java.util.*;

public class 좋다_1253 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] nums = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(nums);

        int answer = 0;
        for (int i = 0; i < N; i++) {
            int a = 0;
            int b = N - 1;
            long target = nums[i];
            while (a < b) {
                long sum = nums[a] + nums[b];
                if (sum == target) {
                    if (a != i && b != i) {
                        answer++;
                        break;
                    } else if (a == i) {
                        a++;
                    } else if (b == i) {
                        b--;
                    }
                } else if (sum < target) {
                    a++;
                } else {
                    b--;
                }
            }
        }
        System.out.println(answer);
    }
}
