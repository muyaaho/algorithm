import java.util.*;

class Solution {
    boolean[] visited;
    Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        Set<Integer> set = new HashSet<>();

        // graph 만들기
        for(int[] nodes: wires) {
            int a = nodes[0], b = nodes[1];
            set.add(a);
            set.add(b);
            graph.computeIfAbsent(a, key -> new ArrayList<>()).add(b);
            graph.computeIfAbsent(b, key -> new ArrayList<>()).add(a);
        }

        // answer 업데이트
        for (int[] cut: wires) {
            visited = new boolean[101];
            int[] tmp = new int[2];
            int tmpIdx = 0;

            for (int node : set) {
                if (!visited[node]) {
                    tmp[tmpIdx++] = bfs(cut[0], cut[1], node);
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

            List<Integer> nextNodes = graph.get(now);
            for (int i = 0; i < nextNodes.size(); i++) {
                int next = nextNodes.get(i);

                if (!(now == cutA && next == cutB || now == cutB && next == cutA) && !visited[next]) {
                    q.offer(next);
                    visited[next] = true;
                }
            }
        }

        return count;
    }
}