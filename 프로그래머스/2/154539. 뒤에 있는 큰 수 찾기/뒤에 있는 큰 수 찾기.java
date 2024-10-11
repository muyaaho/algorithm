class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;
        int[] answer = new int[len];
        
        answer[len-1] = -1;
        for (int i = len-2; i >= 0; i--) {
            if (numbers[i] < numbers[i + 1]) {
                answer[i] = numbers[i+1]; 
            }
            
            else {
                int next = i+1;
                while (!(numbers[i] < answer[next] || answer[next] == -1)) {
                    next ++;
                }
                answer[i] = answer[next];
            }
        }
        return answer;
    }
}