package boj.silver;

import java.io.*;
import java.util.*;

public class 예산_2512 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] budgets = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            budgets[i] = Integer.parseInt(st.nextToken());
        }
        int totalBudget = Integer.parseInt(br.readLine());
        
        Arrays.sort(budgets);
        int start = 0;
        int end = budgets[N-1];
        int answer = 0;

        while (start <= end) {
            int mid = (start + end) / 2;
            int total = 0;
            for (int b : budgets) {
                if (b < mid) {
                    total += b;
                }
                else {
                    total += mid;
                }
            }

            if (total > totalBudget) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
                answer = mid;
            }
        }

        System.out.println(answer);

        br.close();
    }
}
