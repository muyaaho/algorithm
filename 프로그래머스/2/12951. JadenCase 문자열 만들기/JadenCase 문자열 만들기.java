class Solution {
    public String solution(String s) {
        String answer = "";
        
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (i == 0 || s.charAt(i-1) == ' ') {
                answer += Character.toUpperCase(now);
                continue;
            }
            
            if (Character.isUpperCase(now)) {
                answer += Character.toLowerCase(now);
                continue;
            }
            
            answer += now;
        }
        
        return answer;
    }
}