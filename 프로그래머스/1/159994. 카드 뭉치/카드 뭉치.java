class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        int c1Idx = 0, c2Idx = 0;
        // System.out.println(goal[0].compareTo(cards1[c1Idx]));
        for(String word : goal) {
            if (c1Idx < cards1.length && word.compareTo(cards1[c1Idx]) == 0) {
                c1Idx ++;
                continue;
            }
            if (c2Idx < cards2.length && word.compareTo(cards2[c2Idx]) == 0) {
                c2Idx ++;
                continue;
            }
            answer = "No";
            break;
    
        }
        return answer;
    }
}