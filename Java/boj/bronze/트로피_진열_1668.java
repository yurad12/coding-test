package boj.bronze;

import java.util.Scanner;

public class 트로피_진열_1668 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] trophies = new int[N];
        for (int i = 0; i < N; i++) {
            trophies[i] = sc.nextInt();
        }

        // left
        int leftCount = 0;
        int leftMax = 0;
        for (int i = 0; i < N; i++) {
            if (trophies[i] > leftMax) {
                leftMax = trophies[i];
                leftCount++;
            }
        }

        // right
        int rightCount = 0;
        int rightMax = 0;
        for (int i = N-1; i >= 0; i--) {
            if (trophies[i] > rightMax) {
                rightMax = trophies[i];
                rightCount++;
            }
        }

        System.out.println(leftCount);
        System.out.println(rightCount);

        sc.close();
    }
}
