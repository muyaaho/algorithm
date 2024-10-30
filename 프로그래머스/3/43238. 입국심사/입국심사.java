import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        int arrlen = times.length;

        long min = 0;
        long max = 1_000_000_000 * (long) n;
        
        while (min <= max) {
            long target = (min + max) / 2;
            long people = 0;
            for (int time : times) {
                people += (target / time);
            }
            
            if (people < n) {
                min = target + 1;
            } else {
                max = target - 1;
                answer = target;
            }
        }
        return answer;
    }
}