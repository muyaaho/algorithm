import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr1 = new int[n];
        String[] inpline = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr1[i] = Integer.parseInt(inpline[i]);
        }

        int m = Integer.parseInt(br.readLine());
        inpline = br.readLine().split(" ");
        int[] arr2 = new int[m];
        for (int i = 0; i < m; i++) {
            arr2[i] = Integer.parseInt(inpline[i]);
        }

        // System.out.println(Arrays.toString(arr2));

        Arrays.sort(arr1);
        // Arrays.sort(arr2);
        // System.out.println("arr1: "+Arrays.toString(arr1));
        
        for (int x:arr2) {
            // System.out.println("x: "+x);
            int min = 0, max = n-1;
            int ans = 0;
            while (min <= max) {
                
                int mid = (min + max) / 2;
                // System.out.println("min: "+min+", max: "+max+", mid: "+mid);

                // 배열에 있는게 입력보다 크면 배열 인덱스를 줄여야겠죠?
                if (arr1[mid] <= x) {
                    // System.out.println("mid: "+mid+", arr[mid]: "+arr1[mid]);
                    min = mid+1;
                    ans = arr1[mid];
                }
                else {
                    max = mid-1;
                }
            }
            if (ans == x)
                System.out.print("1 ");
            else
                System.out.print("0 ");
        }

    }
}