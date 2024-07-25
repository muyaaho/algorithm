class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (i == 0 || s.charAt(i-1) == ' ') {
                answer.append(Character.toUpperCase(now));
                continue;
            }

            if (Character.isUpperCase(now)) {
                answer.append(Character.toLowerCase(now));
                continue;
            }

            answer.append(now);
        }

        return answer.toString();
    }
}