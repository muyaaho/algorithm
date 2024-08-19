import java.util.*;
class Solution {
    public static int solution(String s) {
        int answer = -0;

        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < s.length(); i++) {
            char start = sb.charAt(0);
            sb.deleteCharAt(0);
            sb.append(start);
            // System.out.println("sb = " + sb);
            if (process(sb.toString())) {
                answer++;
            }

        }

        return answer;
    }

    private static boolean process(String s) {
        Stack<String> stack = new Stack<>();
        for (String x : s.split("")) {

            if (x.equals("]") || x.equals("}") || x.equals(")")) {
                check(x, stack);
                continue;
            }
            stack.push(x);

        }
        return stack.empty();
    }

    private static void check(String now, Stack<String> stack) {
        Map<String, String> map = new HashMap<>();
        map.put(")", "(");
        map.put("]", "[");
        map.put("}", "{");
        if (!stack.empty() && stack.peek().equals(map.get(now))) {
            stack.pop();
        }
        else {
            stack.push(now);
        }
    }
}