import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Map<String, Integer> map = new HashMap<>();
        //System.out.println(participant.length);
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        
        for (String c : completion) {
            map.computeIfPresent(c, (k, v) -> v-1 == 0 ? null : v-1);
        }
        
        for (String a: map.keySet()) {
            answer = a;
        }
        return answer;
    }
}