import java.util.*;
import java.io.*;

class Main {

    static ArrayList<String> answer = new ArrayList<>();
    static Map<String, Integer> map = Map.of("<", -1, ">", 1);
    static String[] checks;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        checks = new String[k];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            checks[i] = st.nextToken();
        }

        for (int start = 0; start < 10; start ++) { 
            boolean[] visited = new boolean[10];
            visited[start] = true;
            dfs(1, k, new ArrayList<>(Arrays.asList(start)), visited);
        }

        Collections.sort(answer);
        System.out.println(answer.get(answer.size()-1));
        System.out.println(answer.get(0));
    
    }

    public static void dfs(int size, int k, ArrayList<Integer> tmp, boolean[] visited) {
        if (size - 1 == k) {
            StringBuilder sb = new StringBuilder();
            for (Integer x : tmp) {
                sb.append(Integer.toString(x));
            }
            answer.add(sb.toString());
            return ;
        }

        for (Integer next = 0; next < 10; next++) {
            if (map.get(checks[size - 1]) == Integer.compare(tmp.get(size-1), next) && !visited[next]) {
                tmp.add(next);
                visited[next] = true;
                dfs(size + 1, k, tmp, visited);
                tmp.remove(next);
                visited[next] = false;
            }
        }
    }
}