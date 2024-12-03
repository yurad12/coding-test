package boj.silver;

import java.io.*;
import java.util.StringTokenizer;

public class 배열_합치기_11728 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] B = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        int i = 0;
        int j = 0;
        StringBuilder sb = new StringBuilder();

        while (i < N && j < M) {
            if (A[i] < B[j]) {
                sb.append(A[i]).append(" ");
                i++;
            }
            else {
                sb.append(B[j]).append(" ");
                j++;
            }
        }

        while (i < N) {
            sb.append(A[i]).append(" ");
            i++;
        }
        
        while (j < M) {
            sb.append(B[j]).append(" ");
            j++;
        }

        System.out.println(sb.toString().strip());

    }
}
