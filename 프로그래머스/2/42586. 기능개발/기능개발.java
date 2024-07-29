import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<Integer> tmp = new ArrayList<>();

        int size = speeds.length;
        Integer[] stack = new Integer[size];

        int leftDay = 0, leftProgress = 0;
        for (int i = 0; i < size; i++) {
            leftProgress = 100 - progresses[i];
            if (leftProgress % speeds[i] > 0) {
                leftDay = (int)(leftProgress / speeds[i]) + 1;
            }
            else 
                leftDay = (int)(leftProgress / speeds[i]);

            stack[i] = leftDay;

        }
        // Arrays.sort(stack);
        // System.out.println(Arrays.toString(stack));
        
        int maxValue = 0;
        for (int i = 0; i < size; i++) {
            if (i == 0) {
                tmp.add(stack[i]);
                maxValue = stack[i];
                continue;
            }
            
            // System.out.println(maxValue+", "+ stack[i]);
            if (maxValue < stack[i]) {
                answer.add(tmp.size());
                tmp.clear();
                maxValue = stack[i];
                tmp.add(stack[i]);
                continue;
            }
            tmp.add(stack[i]);
            maxValue = Math.max(maxValue, stack[i]);
        }
        
        if (!tmp.isEmpty()) 
            answer.add(tmp.size());
        
        // System.out.println(answer.toString());
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}