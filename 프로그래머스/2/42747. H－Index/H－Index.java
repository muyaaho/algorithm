import java.util.*;
class Solution {
    public static int solution(int[] citations) {
        int answer = 0;
        Integer[] integerArr = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(integerArr, Comparator.reverseOrder());
        for (int i = 0; i < integerArr.length; i++) {
            if (i >= integerArr[i])
                return i;
        }
        return integerArr.length;
    }
}