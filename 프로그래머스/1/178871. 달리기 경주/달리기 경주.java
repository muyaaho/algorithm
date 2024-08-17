import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        
        
        for (String calling : callings) {
            Integer index = map.get(calling);
            String tmp = players[index-1];
            players[index - 1] = players[index];
            players[index] = tmp;
            map.put(calling, index-1);
            map.put(tmp, index);
        }

        return players;
    }
}