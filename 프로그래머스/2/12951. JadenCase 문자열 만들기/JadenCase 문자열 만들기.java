class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        s = s.toLowerCase();

        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            answer.append(i == 0 || s.charAt(i-1) == ' ' ? Character.toUpperCase(now) : now);
        }
        return answer.toString();
    }
}