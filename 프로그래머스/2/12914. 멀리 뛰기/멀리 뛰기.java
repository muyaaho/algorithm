class Solution {
    public long solution(int n) {
        long answer = 0;
        int[] dp = new int[n+1];
        if (n <= 3) {
            return (long) n;
        }
        
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < n+1; i++) {
            dp[i] = (dp[i-1]+dp[i-2]) % 1234567;
        }
        return (long) dp[n];
    }
}