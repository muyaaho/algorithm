import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arrN = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arrN[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        int[] arrM = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            arrM[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arrN);
        // System.out.println(Arrays.toString(arrN));
        StringBuilder sb = new StringBuilder();
        for (int x : arrM) {
            // System.out.println("x: "+x);
            int start = 0, end=n-1;
            int leftIndex = -1;
            while (start <= end) {
                int mid = (start + end) / 2;
                // System.out.println("start: "+start+", end: "+end+", mid:"+mid);
                
                if (x == arrN[mid]) {
                    if (mid > 0 && arrN[mid-1] == x) {
                        end = mid-1;
                        continue;
                    } 
                    leftIndex = mid;
                    break;
                }
                else if (x <= arrN[mid]) {
                    end = mid-1;
                } else {
                    start = mid+1;
                }
            }
            start = 0;
            end=n-1;
            int rightIndex = -1;
            while (start <= end) {
                int mid = (start + end) / 2;
                // System.out.println("start: "+start+", end: "+end+", mid:"+mid);
                
                if (x == arrN[mid]) {
                    if (mid < n-1 && arrN[mid + 1] == x) {
                        start = mid+1;
                        continue;
                    }
                    rightIndex = mid;
                    break;
                }
                else if (x < arrN[mid]) {
                    end = mid-1;
                } else {
                    start = mid+1;
                }
            }
            if (rightIndex > -1 && leftIndex > -1) 
                sb.append((rightIndex - leftIndex+1)).append(" ");
            else
                sb.append(0).append(" ");


        }
        System.out.println(sb.toString());
        
    }
}