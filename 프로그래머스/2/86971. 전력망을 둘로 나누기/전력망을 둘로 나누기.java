import java.util.*;

class Solution {
    boolean[] visited;
    Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        Set<Integer> set = new HashSet<>();
        
        // graph 만들기
        for(int[] x: wires) {
            int a = x[0], b = x[1];
            set.add(a);
            set.add(b);
            graph.computeIfAbsent(a, key -> new ArrayList<>()).add(b);
            graph.computeIfAbsent(b, key -> new ArrayList<>()).add(a);
        }
        
        // answer 업데이트
        for (int[] x: wires) {
            int cutA = x[0], cutB = x[1];
            visited = new boolean[Collections.max(set) + 1];
            int[] tmp = new int[2];
            int tmpIdx = 0;
            
            for (int node : set) {
                if (!visited[node]) {
                    tmp[tmpIdx++] = bfs(cutA, cutB, node);
                }
            }
            answer = Math.min(answer, Math.abs(tmp[0] - tmp[1]));
        }
        return answer;
    }
    
    private int bfs(int cutA, int cutB, int start) {
        int count = 0;
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(start);
        visited[start] = true;
        
        while (!q.isEmpty()) {
            int now = q.poll();
            count++;
            
            List<Integer> nexts = graph.get(now);
            for (int i = 0; i < nexts.size(); i++) {
                int next = nexts.get(i);
                
                if (!(now == cutA && next == cutB || now == cutB && next == cutA) && !visited[next]) {
                    q.offer(next);
                    visited[next] = true;
                }
                
            }
        }
        
        return count;
    }
}