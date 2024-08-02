import java.util.*;
class Solution {
    static int hIndex;
    public static int solution(int[] citations) {
        hIndex = citations.length;

        while (hIndex >= 0) {
            if (hIndex <= Arrays.stream(citations).filter(x -> x >= hIndex).count()) {
                return hIndex;
            }
            hIndex--;
        }
        return -1;
    }
}