import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int l = 0, r = 0, kind = 0, cnt = 0, ans = 0;
        int[] nums = new int[10];

        while (r < n) {
            if (++nums[arr[r]] == 1)
                kind++;
            cnt++;

            if (2 < kind) {
                if (--nums[arr[l]] == 0)
                    kind--;
                cnt --;
                l ++;
            }

            ans = Math.max(ans, cnt);
            r ++;
        }

        System.out.println(ans);
    }
}