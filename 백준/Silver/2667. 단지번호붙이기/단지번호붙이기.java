import java.util.*;
import java.io.*;
import java.awt.Point;

class Main {

    static Queue<Integer> answer = new PriorityQueue<>();
    static int n;
    static int[][] arr;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split("");
            // System.out.println(Arrays.toString(line));
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(line[j]);
            }
        }
        visited = new boolean[n][n];
        

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 1 && !visited[i][j]) {
                    answer.add(bfs(i, j));
                }
            }
        }
        System.out.println(answer.size());
        while (!answer.isEmpty())
            System.out.println(answer.poll());
    }

    private static int bfs(int i, int j) {
        Deque<Point> q = new ArrayDeque<>();
        q.offer(new Point(i, j));
        visited[i][j] = true;
        int count = 0;

        while (!q.isEmpty()) {
            Point point = q.poll();
            count++;

            int nx = 0, ny = 0;
            for (int k = 0; k < 4; k++) {
                nx = point.x + dx[k];
                ny = point.y + dy[k];

                if ((0 <= nx && nx < n) && (0 <= ny && ny < n)) {
                    if (arr[nx][ny] == 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                    q.offer(new Point(nx, ny));
                    }
                }
            }
        }
        return count;
    }
}