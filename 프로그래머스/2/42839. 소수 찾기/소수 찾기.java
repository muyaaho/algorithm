import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    String nums = "";
    boolean[] reversePrime;
    int numsSize;
    public int solution(String numbers) {
        numsSize = numbers.length();
        reversePrime = primeArr();
        nums = numbers;
        backtr(0, new boolean[numsSize], new StringBuilder());
        
        return set.size();
    }
    
    private void backtr(int cnt, boolean[] visited, StringBuilder sb) {
        if (sb.length() > 0) {
            int n = Integer.parseInt(sb.toString());
            if (!reversePrime[n]) set.add(n);
        }
        
        if (cnt == numsSize) {    
            return;
        }
        
        for (int i = 0; i < numsSize; i++) {
            if (!visited[i]) {
                visited[i] = true;
                sb.append(nums.charAt(i));
                backtr(cnt+1, visited, sb);
                sb.deleteCharAt(sb.length() -1);
                visited[i] = false;
            }
        }
    }
    
    private boolean[] primeArr () {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numsSize; i++) {
            sb.append('9');
        }
        int primeSize = Integer.parseInt(sb.toString()) + 1;
        
        boolean[] prime = new boolean[primeSize];
        prime[0] = true;
        prime[1] = true;
        
        for (int i = 2; i < primeSize; i++) {
            for (int k = 2*i; k < primeSize; k += i) {
                prime[k] = true;
            }
        }
        return prime;
    }
}