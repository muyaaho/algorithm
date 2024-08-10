import java.util.*;
class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        
        for (String num : number.split("")) {
            int size = answer.length();
            while (k > 0 && size > 0 && answer.charAt(size-1) < num.charAt(0)) {
                answer.deleteCharAt(size-1);
                k --;
                size = answer.length();
            }
            answer.append(num);
        }
        
        return answer.substring(0, answer.length()-k).toString();
    }
}