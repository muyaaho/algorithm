class Solution {
    public int solution(int n) {
        int answer = 0;
        int a = 0, b = 1, tmp = 0;
        
        while (n-- > 0) {
            tmp = b;
            b = (a + b) % 1234567;
            a = tmp;
        }
        return a % 1234567;
    }
}