import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int sol(String[] inp) {
        int m = Integer.parseInt(inp[0]);
        int n = Integer.parseInt(inp[1]);
        int x = Integer.parseInt(inp[2]);
        int y = Integer.parseInt(inp[3]);

        int k = x;

        while (k <= m * n) {
            if ((k - x) % m == 0 && (k - y) % n == 0) {
                return k;
            }
            k += m;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            String[] arr = br.readLine().split(" ");
//            System.out.println(Arrays.toString(arr));
            System.out.println(sol(arr));
        }
    }
}
