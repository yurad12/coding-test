package boj.silver;

import java.io.*;
import java.util.*;

public class 나이트의_이동_7562 {
    static class Node {
        int x;
        int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T > 0) {
            T -= 1;

            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());

             st = new StringTokenizer(br.readLine());
            int endX = Integer.parseInt(st.nextToken());
            int endY = Integer.parseInt(st.nextToken());

            int[][] direc = {{-2,-1}, {-2,1}, {-1,2}, {-1,-2}, {1,-2}, {1,2}, {2,-1}, {2,1}};
            int answer = 0;

            ArrayDeque<Node> q = new ArrayDeque<>();
            int[][] visited = new int[n][n];
            visited[startX][startY] = 1;


            q.addLast(new Node(startX, startY));

            while (!q.isEmpty()) {
                Node now = q.removeFirst();
                if (now.x == endX && now.y == endY) {
                    answer = visited[now.x][now.y] - 1;
                    break;
                }

                for (int[] d : direc) {
                    int nx = now.x + d[0];
                    int ny = now.y + d[1];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny] != 0) {
                        continue;
                    }

                    q.addLast(new Node(nx, ny));
                    visited[nx][ny] = visited[now.x][now.y] + 1;
                }
            }

            System.out.println(answer);
        }

        br.close();
    }
}
