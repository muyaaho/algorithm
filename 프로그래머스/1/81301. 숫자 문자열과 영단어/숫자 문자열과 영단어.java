class Solution {
    public int solution(String s) {
        
        // map 대신 String array
        String[] nums = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        StringBuilder answer = new StringBuilder();
        int now = 0;
        while (now < s.length()) {
            if ('0' <= s.charAt(now) && s.charAt(now) <= '9') {
                answer.append(s.charAt(now));
                now += 1;
            }
            for (int i = 0; i < 10; i++) {
                int end = now + nums[i].length();
                if (end < s.length() + 1 && nums[i].equals(s.substring(now, end))) {
                    answer.append(i);
                    now += nums[i].length();
                    break;
                }
            }
        }
        return Integer.parseInt(answer.toString());
    }
}