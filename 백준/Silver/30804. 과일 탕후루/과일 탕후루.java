import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int l = 0, r = 0, cnt = 0, kind = 0, ans = 0;
        int[] nums = new int[10];

        while (r < n) {
            if (nums[arr[r]] == 0)
                kind ++;
            cnt ++;
            nums[arr[r]] ++;

            if (kind > 2) {
                if (--nums[arr[l]] == 0)
                    kind --;
                l++;
                cnt--;
            }

            ans = Math.max(cnt, ans);
            r ++;
        }

        System.out.println(ans);

    }
}
