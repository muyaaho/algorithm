import java.util.*;
import java.awt.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int col = maps.length;
        int row = maps[0].length;
        
        int[][] cost = new int[col][row];
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                cost[i][j] = Integer.MAX_VALUE;
            }
        }
        
        Deque<Point> q = new ArrayDeque<>();
        q.offer(new Point(0, 0));
        cost[0][0] = 1;
        
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        while (!q.isEmpty()) {
            Point now = q.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + now.x;
                int ny = dy[i] + now.y;
                
                if (0 <= nx && nx < col && 0 <= ny && ny < row) {
                    if (maps[nx][ny] == 1 && cost[nx][ny] > cost[now.x][now.y] + 1) {
                        q.offer(new Point(nx, ny));
                        cost[nx][ny] = cost[now.x][now.y] + 1;
                    }
                }
            }
        }
        
        return cost[col - 1][row - 1] != Integer.MAX_VALUE ? cost[col - 1][row - 1] : -1;
    }
}