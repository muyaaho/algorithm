import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int answer = 0;
        
        for (int x : scoville) 
            heap.offer(x);

        while (heap.size() > 1 && heap.peek() < K) {
            heap.offer(heap.poll() + heap.poll() * 2);
            answer ++;
            continue;
        }
        
        return heap.poll() < K ? -1 : answer;
    }
}