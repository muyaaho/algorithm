import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        TreeMap<Integer, Integer> q = new TreeMap<>();
        
        for (String e : operations) {
            String[] arr = e.split(" ");
            char cmd = arr[0].charAt(0);
            int num = Integer.parseInt(arr[1]);
            
            if (cmd == 'I') {
                q.put(num, q.getOrDefault(num, 0) + 1);
                continue;
            }
            
            if (q.isEmpty())
                continue;
            
            int delNum = num == 1 ? q.lastKey(): q.firstKey();
            if (q.put(delNum, q.get(delNum) - 1) == 1)
                q.remove(delNum);
                
        }
        
        if (q.isEmpty()) {
            return answer;
        }
        answer[0] = q.lastKey();
        answer[1] = q.firstKey();
        
        return answer;
    }
}