import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    String nums = "";
    boolean[] prime;
    public int solution(String numbers) {
        int answer = 0;
        int numSize = numbers.length();
        prime = primeArr(numSize);
        nums = numbers;
        backtr(numSize, 0, new boolean[numSize], new StringBuilder());
        
        
        // System.out.println(set);
        
        
        
        return set.size();
    }
    
    private void backtr(int maxLen, int cnt, boolean[] visited, StringBuilder sb) {
        if (sb.length() > 0) {
            int n = Integer.parseInt(sb.toString());
        if (prime[n])
            set.add(n);
        }
        
        
        if (cnt == maxLen) {    
            return;
        }
        
        for (int i = 0; i < maxLen; i++) {
            if (!visited[i]) {
                visited[i] = true;
                sb.append(nums.charAt(i));
                backtr(maxLen, cnt+1, visited, sb);
                sb.deleteCharAt(sb.length() -1);
                visited[i] = false;
            }
        }
        
        
    }
    
    private boolean[] primeArr (int numSize) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numSize; i++) {
            sb.append('9');
        }
        int primeSize = Integer.parseInt(sb.toString()) + 1;
        
        boolean[] prime = new boolean[primeSize];
        for (int i = 0; i < primeSize; i++) {
            prime[i] = true;
        }
        prime[0] = false;
        prime[1] = false;
        
        for (int i = 2; i < primeSize; i++) {
            if (!prime[i]) continue;
            for (int k = 2*i; k < primeSize; k += i) {
                prime[k] = false;
            }
        }
        return prime;
    }
}