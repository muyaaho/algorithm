import java.util.*;
import java.awt.Point;

class Solution {
    int answer = 0;
    public int solution(int n) {
        for (int j = 0; j < n; j++) {
            boolean[][] visited = new boolean[n][n];
            ArrayList<Point> deleted = check(n, visited, 0, j);
            for (Point p : deleted) {
                visited[p.x][p.y] = true;
            }
            backtrk(n, 0, j, 1, visited);
        }
        return answer;
    }
    
    private ArrayList<Point> check(int n, boolean[][] visited, int x, int y) {
        // 가로
        ArrayList<Point> arr = new ArrayList<>();
        for (int k = y+1; k < n; k++) {
            if (!visited[x][k]) {
                arr.add(new Point(x, k));
            }
        }

        // 세로
        for (int k = x+1; k < n; k++) {
            if (!visited[k][y]) {
                arr.add(new Point(k, y));
            }
        }

        // 왼쪽 아래 대각선            
        int ni = x+1, nj = y-1;
        while (ni < n && nj >= 0) {
            if (!visited[ni][nj])
                arr.add(new Point(ni, nj));
            ni++;
            nj--;

        }

        // 오른쪽 아래 대각선
        ni = x+1;
        nj = y+1;
        while (ni < n && nj < n) {
            if (!visited[ni][nj])
                arr.add(new Point(ni, nj));
            ni++;
            nj++;
        }
        
        return arr;
    }
    
    public void backtrk(int n, int x, int y, int cnt, boolean[][] visited) {
        
        if (x+1 == n) {
            if (cnt == n) {
                answer ++;
            }
            return;
        }
        
        for (int ny = 0; ny < n; ny++) {
            if (!visited[x+1][ny]) {    
                ArrayList<Point> deleted = check(n, visited, x+1, ny);
                for (Point p: deleted) {
                    visited[p.x][p.y] = true;
                }
                backtrk(n, x+1, ny, cnt+1, visited);
                for (Point p: deleted) {
                    visited[p.x][p.y] = false;
                }
            }
        }
    }
}