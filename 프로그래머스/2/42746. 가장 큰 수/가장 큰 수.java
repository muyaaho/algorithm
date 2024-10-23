import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder sb = new StringBuilder();
        String[] strArr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strArr[i] = Integer.toString(numbers[i]);
        }
        
        Arrays.sort(strArr, (o1, o2) -> o2.repeat(3).compareTo(o1.repeat(3)));
        for (String x : strArr) {
            sb.append(x);
        }
        
        String answer = sb.toString();
        
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}