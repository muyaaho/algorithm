import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

class Main {

    static Map<Integer, String> cmdMap = Map.of(0, "D", 1, "S", 2, "L", 3, "R");
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T -- > 0) {
            String[] arr = br.readLine().split(" ");
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);

            Queue<Tuple> q = new LinkedList<>();
            q.add(new Tuple(a, ""));
            boolean[] visited = new boolean[10000];
            visited[a] = true;

            while (!q.isEmpty()) {
                Tuple now = q.poll();

                if (now.num == b) {
                    System.out.println(now.cmd);
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int newNum = process(i, now.num);
                    if (! visited[newNum]) {
                        visited[newNum] = true;
                        q.add(new Tuple(newNum, now.cmd+cmdMap.get(i)));
                    }
                }
            }

        }

    }

    private static int process(int i, int x) {
        if (i == 0)
            return (x * 2) % 10000;
        if (i == 1)
            return x == 0 ? 9999 : x - 1;
        if (i == 2)     // 1234 -> 2341 
            return (x % 1000) * 10 + x / 1000;
        // 1234 -> 4123
        return (x % 10) * 1000 + x / 10;
    }
}

class Tuple {
    int num;
    String cmd;

    public Tuple(int num, String cmd) {
        this.num = num;
        this.cmd = cmd;
    }
}