import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        Arrays.sort(plans, Comparator.comparing(o -> o[1]));
        Deque<Box> stack = new ArrayDeque<>();

        int past = 0, i = 0;
        for (String[] x: plans) {
            int now = changeMinute(x[1]);
            int playtime = Integer.parseInt(x[2]);

            if (stack.isEmpty()) {
                stack.push(new Box(x[0], playtime));
                past = now;
                continue;
            }
            int passed = now - past;
            past = now;

            while (!stack.isEmpty() && stack.peek().rest <= passed) {
                Box deleted = stack.pop();
                answer[i++] = deleted.subject;
                passed -= deleted.rest;
            }

            if (!stack.isEmpty() && stack.peek().rest > passed) {
                stack.peek().rest -= passed;
            }
            stack.push(new Box(x[0], playtime));
        }

        while (!stack.isEmpty()) {
            answer[i++] = stack.pop().subject;
        }

        return answer;
    }

    public int changeMinute(String time) {
        String[] arr = time.split(":");
        return Integer.parseInt(arr[0]) * 60 + Integer.parseInt(arr[1]);
    }

    class Box {
        String subject;
        int rest;

        public Box(String subject, int rest) {
            this.subject = subject;
            this.rest = rest;
        }
    }
}