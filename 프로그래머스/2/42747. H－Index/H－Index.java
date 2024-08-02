import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        
        // System.out.println(Arrays.toString(citations));
        
        for (int hIndex = citations.length; hIndex >= 0; hIndex--) {
            int cnt = 0;
            for (int x : citations) {
                if (x >= hIndex) {
                    cnt ++;
                }
            }
            if (hIndex <= cnt) {
                answer = hIndex;
                break;
            }
        }
                
        return answer;
    }
}