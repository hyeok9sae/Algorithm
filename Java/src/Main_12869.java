import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_12869 {   // 뮤탈리스크
    static int[] scv;
    static int[] mut = {9, 3, 1};
    static int[][] atk;
    static int pn = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        scv = new int[3];
        atk = new int[6][3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int n = 0; n < N; n++){
            scv[n] = Integer.parseInt(st.nextToken());
        }
        if (scv.length == 1){
            scv[1] = 0;
            scv[2] = 0;
        } else if(scv.length == 2){
            scv[2] = 0;
        }
//        int[] mutali = new int[N];
//        for (int n = 0; n < N; n++){
//            mutali[n] = mut[n];
//        }
        permutation(mut, 0, 3, 3);
        bfs();
    }
    public static void bfs(){
        Queue<int[]> que = new LinkedList<>();
        boolean visited[][][] = new boolean[61][61][61];
        int cnt = 0;
        que.offer(new int[]{scv[0], scv[1], scv[2], cnt});
        while (!que.isEmpty()){
            int[] tmp = que.poll();
            for (int i = 0; i < 6; i++){
                int n1 = tmp[0] - atk[i][0];
                int n2 = tmp[1] - atk[i][1];
                int n3 = tmp[2] - atk[i][2];
                if (n1 < 0){
                    n1 = 0;
                }
                if (n2 < 0){
                    n2 = 0;
                }
                if (n3 < 0){
                    n3 = 0;
                }
                int n4 = tmp[3];
//                System.out.println(n1+" "+n2+" "+n3+" "+n4);
                if (n1 <= 0 && n2 <= 0 && n3 <= 0){
                    System.out.println(n4+1);
                    return;
                }
                if (visited[n1][n2][n3]){
                    continue;
                }
                visited[n1][n2][n3] = true;
                que.offer(new int[]{n1, n2, n3, n4+1});

            }

        }
    }

    public static void permutation(int[] arr, int depth, int n, int r) {
        if (depth == r) {
            if (arr.length == 1){
                for (int i = 0; i < arr.length; i++){
                    atk[pn][i] = arr[i];
                }
                atk[pn][1] = arr[1];
                atk[pn][2] = arr[2];
            } else if(arr.length == 2){
                for (int i = 0; i < arr.length; i++){
                    atk[pn][i] = arr[i];
                }
                atk[pn][2] = arr[2];
            } else if(arr.length == 3){
                for (int i = 0; i < arr.length; i++){
                    atk[pn][i] = arr[i];
                }
            }
            pn++;
            return;
        }

        for (int i=depth; i<n; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }
}