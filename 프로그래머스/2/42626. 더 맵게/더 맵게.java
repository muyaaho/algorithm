import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int answer = 0;
        
        for (int i = 0; i < scoville.length; i++) {
            heap.add(scoville[i]);
        }
        // System.out.println(heap.peek());
        // System.out.println(heap.size());
        
        while (heap.size() > 1) {
            if (heap.peek() < K) {
                heap.offer(heap.poll() + heap.poll() * 2);
                answer ++;
                continue;
            }
            break;
        }
        
        return heap.poll() >= K ? answer : -1;
    }
}