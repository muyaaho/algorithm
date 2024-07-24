import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Map;
import java.util.Queue;
import java.util.LinkedList;

class Main {
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        Map<Integer, String> d = Map.of(0, "D", 1, "S", 2, "L", 3, "R");

        for (int tc = 0; tc < t; tc++) {
            String[] inputArr = br.readLine().split(" ");
            int a = Integer.parseInt(inputArr[0]);
            int b = Integer.parseInt(inputArr[1]);
            
            Queue<Register> q = new LinkedList<>();
            q.add(new Register(a, ""));
            visited = new boolean[10000];
            visited[a] = true;

            while (!q.isEmpty()) {
                Register now = q.poll();

                if (now.num == b) {
                    System.out.println(now.cmd);
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int nextNum = fun(now.num, i);

                    if (!visited[nextNum]) {
                        visited[nextNum] = true;
                        q.add(new Register(nextNum, now.cmd+d.get(i)));
                    }
                }
            }

        }
    }

    private static int fun(int x, int i) {
        if (i == 0)
            return (x*2) % 10000;
        if (i == 1)
            return x == 0 ? 9999 : (x-1) % 10000;
        if (i == 2)
            return x / 1000 + (x % 1000) * 10;
        return x / 10 + (x % 10) * 1000;
    }

    static class Register {
        int num;
        String cmd;

        public Register(int num, String cmd) {
            this.num = num;
            this.cmd = cmd;
        }
    }
}