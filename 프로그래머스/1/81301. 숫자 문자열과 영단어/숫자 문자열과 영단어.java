import java.util.*;
import java.lang.*;

class Solution {
    public int solution(String s) {
        
        Map<String, Character> map = Map.of("zero", '0', "one", '1', "two", '2', "three", '3', "four", '4', "five", '5', "six", '6', "seven", '7', "eight", '8', "nine", '9');
        StringBuilder answer = new StringBuilder();
        int now = 0;
        while (now < s.length()) {
            if (Character.isDigit(s.charAt(now))) {
                answer.append(s.charAt(now));
                now += 1;
            }
            
            for (String word : map.keySet()) {
                int end = now + word.length();
                if (end < s.length() + 1 && word.equals(s.substring(now, end))) {
                    answer.append(map.get(word));
                    now += word.length();
                }
            }
        }
        return Integer.parseInt(answer.toString());
    }
}