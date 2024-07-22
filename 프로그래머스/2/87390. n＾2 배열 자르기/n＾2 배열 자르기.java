
class Solution {
    public int[] solution(int n, long left, long right) {
        int size = (int) (right - left + 1);
        int[] answer = new int[size];
        
        int i = 0, k = 0;
        for (int idx = 0; idx < size; idx ++) {
            i = (int) ((idx+left) / n) ;
            k = (int) ((idx+left) % n);
            
            if (i >= k) 
                answer[idx] = i+1;
            else
                answer[idx] = k+1;
        }
        
        return answer;

    }
}