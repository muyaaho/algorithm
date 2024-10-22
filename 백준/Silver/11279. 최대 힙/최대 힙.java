import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Queue<Integer> q = new PriorityQueue<>((o1, o2) -> o2-o1);


        while (n-- > 0) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (q.isEmpty()) System.out.println(0);
                else System.out.println(q.poll());
                continue;
            }
            q.offer(x);
        }
    }
}