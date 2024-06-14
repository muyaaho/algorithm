import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[6];

        for (int i = 0; i < 6; i++) {
            arr[i] = sc.nextInt();
        }

        int t = sc.nextInt();
        int p = sc.nextInt();

        int answer = 0;
        for (int i = 0; i < 6; i++) {
            answer += arr[i]/t;
            if (arr[i]%t > 0)
                answer++;
        }

        System.out.println(answer);
        System.out.printf("%d %d", n/p, n%p);
        
        sc.close();
    }
}
