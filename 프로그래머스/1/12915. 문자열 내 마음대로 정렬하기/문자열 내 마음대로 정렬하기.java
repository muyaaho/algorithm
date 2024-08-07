import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (x, y) -> x.charAt(n) == y.charAt(n) ? x.compareTo(y) : x.charAt(n) - y.charAt(n));

        return strings;
    }
}