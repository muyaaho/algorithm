import java.util.*;

class Solution {
    public static int solution(int[] people, int limit) {
        int answer = 0;

        ArrayDeque<Integer> arr = new ArrayDeque<>();
        Arrays.sort(people);
        for (int p : people) {
            arr.add(p);
        }
        
        while (!arr.isEmpty()) {
            if (arr.size() > 1) {
                if (arr.getFirst() + arr.getLast() <= limit) {
                    arr.removeFirst();
                    arr.removeLast();
                    answer++;
                    continue;
                }
                arr.removeLast();
                answer++;
            } else {
                answer ++;
                break;
            }
        }
        return answer;
    }
}