import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int m;
    static boolean[] visited;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }
        Arrays.sort(arr);
        visited = new boolean[n];
        sol(new ArrayList<>());


    }

    public static void sol(ArrayList<Integer> tmp) {
        if (tmp.size() == m) {
            tmp.stream().forEach(x -> System.out.print(x+" "));
            System.out.println();
            // System.out.println(tmp.toString());
            return;
        }

        int past = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && arr[i] != past) {
                visited[i] = true;
                past = arr[i];
                tmp.add(arr[i]);
                sol(tmp);
                visited[i] = false;
                tmp.remove(tmp.size()-1);
            }
        }
    }
}