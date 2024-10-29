import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");

        ArrayList<Integer>[] graph = new ArrayList[n];
        
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
            int x = Integer.parseInt(arr[i]);
            if (x == -1) continue;
            graph[x].add(i);
        }

        int[] dp = new int[n];
        
        for (int i = n-1; i > -1; i--) {
            if (graph[i].isEmpty()) {
                dp[i] = 0;
                continue;
            }
            graph[i].sort((o1, o2) -> dp[o2] - dp[o1]);
            
            int update = 0;
            for (int k = 0; k < graph[i].size(); k++) {
                update = Math.max(update, (k+1) + dp[graph[i].get(k)]);
            }
            
            dp[i] = update;
        }

        System.out.println(dp[0]);
    }
}