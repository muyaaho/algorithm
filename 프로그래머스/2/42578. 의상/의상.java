import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        int answer = 1;

        for (String[] clothe : clothes) {
            String key = clothe[1];
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        answer = map.values().stream().reduce(1, (a, b) -> (a * (b+1)));
        // for (int cnt: map.values()) {
        //     answer *= (cnt+1);
        // }
        return answer - 1;
    }
}