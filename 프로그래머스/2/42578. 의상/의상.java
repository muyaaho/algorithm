
/*
1. dict에 값을 저장
2. 1개 ~ dict key의 수만큼 조합 계산
System.out.println(clothes.length);
*/

import java.util.*;

class Solution {
    static Map<String, Integer> map;
    static ArrayList<Integer> results = new ArrayList<>();

    public int solution(String[][] clothes) {
        map = new HashMap<>();
        int answer = 1;
        
        int n = clothes.length;
        for (int i = 0; i< n; i++) {
            String value = clothes[i][0];
            String key = clothes[i][1];
            
            if (!map.containsKey(key)) {
                map.put(key, 1);
            }
            else {
                map.put(key, map.get(key) + 1);
            }
        }
        
        
        int size = map.size();
        Set<String> keys = map.keySet();
        String[] keyArray = keys.toArray(String[]::new);
        for (int i = 0; i < size; i++) {
            answer *= (map.get(keyArray[i])+1);
        }
        


        return answer-1;
    }
    
    
    public static void combination(String[] keys, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            int result = 1;
            for (int i = 0; i< keys.length; i++) {
                if (visited[i])
                    result *= map.get(keys[i]);
            }
            results.add(result);
            return;
        }
        
        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(keys, visited, i+1, n, r-1);
            visited[i] = false;
        }
    }
    
}
