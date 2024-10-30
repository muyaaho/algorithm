import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long min = 0, max = 1_000_000_000 * (long) n;
        
        while (min <= max) {
            long target = (min + max) / 2;
            
            long people = 0;
            for (int time : times) {
                people += (target / time);
            }
            
            if (people < n) {
                min = target + 1;
                continue;
            }
            max = target - 1;
            answer = target;
        }
        return answer;
    }
}