import java.util.*;
import java.awt.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Deque<Point> q = new ArrayDeque<>();
        q.offer(new Point(0, numbers[0]));
        q.offer(new Point(0, -numbers[0]));
        
        while (!q.isEmpty()) {
            Point now = q.poll();
            
            if (now.x == numbers.length - 1) {
                if (now.y == target) answer ++;
                continue;
            }
            
            for (int i = -1; i <= 1; i += 2) {
                if (now.x + 1 < numbers.length) {
                    int next = numbers[now.x+1] * i;
                    q.offer(new Point(now.x+1, now.y+next));
                }
            }
            
        }
        return answer;
    }
}