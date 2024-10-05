import java.util.*;
import java.awt.Point;
import java.lang.*;

class Solution {

    boolean[][] visited;
    int[][] graph;
    int row;
    int col;

    public ArrayList<Integer> solution(String[] maps) {
        ArrayList<Integer> answer = new ArrayList<>();

        col = maps.length;
        row = maps[0].length();
        graph = new int[col][row];
        for(int i = 0; i < col; i++) {
            String[] line = maps[i].split("");

            for (int j = 0; j < row; j++) {
                if (line[j].equals("X")) graph[i][j] = -1;
                else graph[i][j] = Integer.parseInt(line[j]);
            }
        }

        visited = new boolean[col][row];
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (graph[i][j] != -1 && !visited[i][j]) {
                    answer.add(bfs(i, j));
                }
            }
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        }

        Collections.sort(answer);
        return answer;

    }

    private int bfs(int x, int y) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        Deque<Point> q = new ArrayDeque<>();
        visited[x][y] = true;
        q.add(new Point(x, y));
        int days = graph[x][y];

        while (!q.isEmpty()) {
            Point now = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (0 <= nx && nx < col && 0 <= ny && ny < row && !visited[nx][ny] && graph[nx][ny] != -1) {
                    q.add(new Point(nx, ny));
                    visited[nx][ny] = true;
                    days += graph[nx][ny];
                }
            }
        }
        return days;
    }
}