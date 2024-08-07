import java.util.*;
import java.io.*;

class Main {
    static int n, start, target, m;
    static Map<Integer, List<Integer>> graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());

        m = Integer.parseInt(br.readLine());

        graph = new HashMap<>();
        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            List<Integer> k1 = graph.getOrDefault(a, new ArrayList<Integer>());
            k1.add(b);
            graph.put(a, k1);

            List<Integer> k2 = graph.getOrDefault(b, new ArrayList<Integer>());
            k2.add(a);
            graph.put(b, k2);
        }
        System.out.println(bfs());
        
        
    }

    private static int bfs() {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        int[] distance = new int[n+1];
        for (int i = 0; i < n+1; i ++) {
            distance[i] = -1;
        }
        distance[start] = 0;

        while (! q.isEmpty()) {
            int now = q.poll();
            
            for (int next : graph.getOrDefault(now, null)) {
                if (distance[next] == -1) {
                    q.offer(next);
                    distance[next] = distance[now] + 1;
                }
            }
        }
        return distance[target];


    }
}