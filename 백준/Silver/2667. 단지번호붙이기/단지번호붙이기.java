import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;


public class Main {
    
    static char[][] graph;
    static int[] dx = new int[]{-1, 1, 0, 0};
    static int[] dy = new int[]{0, 0, -1, 1};
    static int count;

    static void dfs(int x, int y) {
        graph[x][y] = '3';
        count++;
        for (int i = 0; i < 4; i++) {
            int ix = x + dx[i];
            int iy = y + dy[i];

            if (graph[ix][iy] == '1') dfs(ix, iy);
        }
    }
    
    static void getGraph() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        graph = new char[N+2][N+2];

        for (int i = 0; i < N+2; i++) for (int j = 0 ; j < N+2; j++) graph[i][j] = 'x';

        for (int i = 0; i < N; i++) {
            char[] arr = br.readLine().toCharArray();
            for (int j  = 0; j < N; j++) {
                graph[i+1][j+1] = arr[j];
            }
        }
        
    }

    public static void main(String[] args) throws IOException{

        PriorityQueue<Integer> arr = new PriorityQueue<>();
        int village = 0;

        getGraph();

        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph.length; j++) {
                if (graph[i][j] == '1') {
                    count = 0;
                    village++;
                    dfs(i, j);
                    arr.add(count);
                }
            }
        }

        System.out.println(village);
        while(!arr.isEmpty()) System.out.println(arr.poll());

    }
}
