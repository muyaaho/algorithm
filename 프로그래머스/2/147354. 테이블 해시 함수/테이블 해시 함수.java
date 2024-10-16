import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> {
            if (o1[col-1] != o2[col-1]) {
                return o1[col-1] - o2[col-1];
            }
            return o2[0] - o1[0];
        });
        
        for (int[] tuple : data) {
            q.offer(tuple);
        }
        
        int i = 0;
        while (!q.isEmpty() && i < row_end){
            int[] now = q.poll();
            if (i >= row_begin - 1) {

                int si = 0;
                for (int x : now) {
                    si += (x % (i + 1));
                }                
                
                if (i == row_begin - 1) answer = si;
                else answer ^= si;
            }
            
            i++;
        }

        return answer;
    }
}