import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        int answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] graph = new int[n];

        for(int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(st.nextToken());
        }

        int start = Integer.parseInt(br.readLine());

        Deque<Integer> q = new ArrayDeque<>();
        q.add(start - 1);
        boolean[] visited = new boolean[n];
        visited[start - 1] = true;

        while (!q.isEmpty()) {
            int now = q.poll();
            for (int i = -1; i < 2; i+=2) {
                int next = graph[now] * i + now;

                if (0 <= next && next < n && !visited[next]) {
                    visited[next] = true;
                    q.add(next);
                }
            }
            
        }

        for (boolean x: visited) {
            if (x) answer++;
        }
    
        System.out.println(answer);
    }
}