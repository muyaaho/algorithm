import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder sb = new StringBuilder();
        String[] strArr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strArr[i] = Integer.toString(numbers[i]);
        }
        
        Arrays.sort(strArr, (o1, o2) -> o2.repeat(3).compareTo(o1.repeat(3)));
        boolean isZero = true;
        for (String x : strArr) {
            sb.append(x);
            if (!x.equals("0")) isZero = false;
        }
        
        String answer = sb.toString();
        
        return isZero ? "0" : answer;
    }
}