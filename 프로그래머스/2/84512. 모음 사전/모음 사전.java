import java.util.*;

class Solution {
    TreeSet<String> set = new TreeSet<>();
    String[] vowels = {"A", "E", "I", "O", "U"};
    public int solution(String word) {
        int answer = 0;
        
        for (int i = 1; i <= 5; i++) {
            func(i, new StringBuilder());
        }
        // System.out.println(set);
        List<String> arr = new ArrayList<String>(set);
        return arr.indexOf(word)+1;
    }
    
    private void func(int targetCnt, StringBuilder sb) {
        if (sb.length() == targetCnt) {
            set.add(sb.toString());
            return;
        }
        
        for (int i = 0; i < 5; i++) {
            sb.append(vowels[i]);
            func(targetCnt, sb);
            sb.deleteCharAt(sb.length()-1);
        }
    }
}