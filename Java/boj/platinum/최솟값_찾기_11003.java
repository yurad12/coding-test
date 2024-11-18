package boj.platinum;

import java.io.*;
import java.util.*;

public class 최솟값_찾기_11003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        Deque<Node> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());
            while (!q.isEmpty() && q.getLast().value > now) {
                q.removeLast();
            }
            q.addLast(new Node(now, i));
            if (q.getFirst().index <= i-L) {
                q.removeFirst();
            }
            bw.write(q.getFirst().value + " ");
        }

        bw.flush();
        bw.close();
    }

    static class Node {
        public int value;
        public int index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}
