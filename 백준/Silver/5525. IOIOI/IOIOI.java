//  IOIOI

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int m = Integer.parseInt(bf.readLine());
        String s = bf.readLine();

        int answer = 0, count = 0, i = 0;

        while (i < (m-1)) {
            if (s.startsWith("IOI", i)) {
                count += 1;
                i += 2;
                if (count == n) {
                    answer += 1;
                    count -= 1;
                }
            }
            else {
                count = 0;
                i += 1;
            }
        }
        System.out.println(answer);
    }
}