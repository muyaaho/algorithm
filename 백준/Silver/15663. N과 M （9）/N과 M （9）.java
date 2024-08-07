import java.io.*;
import java.util.*;

class Main {
    static int n, m;
    static int[] arr, perm;
    static boolean[] visited;
    static LinkedHashSet<String> ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        arr = new int[n];
        perm = new int[m];
        visited = new boolean[n];
        ans = new LinkedHashSet<>();

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        permutation(0);
    }

    static void permutation(int cnt) {
        if (cnt == m) {
            StringBuilder sb = new StringBuilder();
            for (int p : perm)
                sb.append(p).append(' ');
            System.out.println(sb.toString());
            return;
        }

        int past = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && arr[i] != past) {
                visited[i] = true;
                perm[cnt] = arr[i];
                permutation(cnt + 1);
                visited[i] = false;
                perm[cnt] = 0;
                past = arr[i];
            }

        }
    }
}