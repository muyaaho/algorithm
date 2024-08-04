import java.io.*;
import java.util.*;

class Main {
    public static int[] arrN;
    public static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] cntArr = new int[20_000_001];

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cntArr[Integer.parseInt(st.nextToken()) + 10_000_000] ++;
        }

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(st.nextToken());
            sb.append(cntArr[x+10_000_000]).append(" ");
        }
        System.out.println(sb);
    }
}