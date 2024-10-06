import java.util.*;
import java.awt.Point;

class Solution {
    int col, row;
    char[][] graph;
    Point start, end;
    public int solution(String[] board) {
        int answer = 0;
        
        col = board.length;
        row = board[0].length();
        
        graph = new char[col][row];
        
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                graph[i][j] = board[i].charAt(j);
                if (graph[i][j] == 'R') {
                    start = new Point(i, j);
                }
                if (graph[i][j] == 'G') {
                    end = new Point(i, j);
                }
            }
        }
        
        return bfs();
    }
    
    private int bfs() {
        Deque<Point> q = new ArrayDeque();
        int[][] dist = new int[col][row];
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        
        dist[start.x][start.y] = 0;
        q.offer(start);
        
        while (!q.isEmpty()) {
            Point now = q.poll();
            if (now.equals(end)) {
                return dist[now.x][now.y];
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = now.x, ny = now.y;
                
                while ((0 <= (nx + dx[i]) && (nx + dx[i]) < col && 0 <= (ny + dy[i]) && (ny + dy[i]) < row) && graph[nx + dx[i]][ny + dy[i]] != 'D') {
                    nx += dx[i];
                    ny += dy[i];
                }
                
                if (dist[nx][ny] > dist[now.x][now.y] + 1) {
                    dist[nx][ny] = dist[now.x][now.y] + 1;
                    q.offer(new Point(nx, ny));
                }
            }
        }
        
        return -1;
    }
}