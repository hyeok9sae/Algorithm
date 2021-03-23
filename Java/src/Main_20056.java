import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_20056 {
    static int[][] arr;
    static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    public static void main(String[] args) throws IOException {
        ArrayList<Data> lst = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
//        System.out.println(M);
        StringTokenizer st2;
        for (int i = 0; i < M; i++){
            st2 = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st2.nextToken());
//            System.out.println(r);
            int c = Integer.parseInt(st2.nextToken());
            int m = Integer.parseInt(st2.nextToken());
            int s = Integer.parseInt(st2.nextToken());
            int d = Integer.parseInt(st2.nextToken());
            lst.add(new Data(r, c, m, s, d));
        }
        for (int i = 0; i < K; i++){
            for (int j = 0; j < M; j++){
                for (int l = 0; l <lst.get(j).s; l++){
                    lst.get(j).r += dy[lst.get(j).d];
                    lst.get(j).r += dx[lst.get(j).d];
                }
            }
            for (int j = 0; j < lst.size(); j++){
                for (int l = 0; l < lst.size(); l++){
                    if (lst.get(j).r == lst.get(l).r && lst.get(j).c == lst.get(l).c){
                        lst.get(j).m = lst.get(j).m + lst.get(l).m
                    }
                }
            }
        }
    }
    public static class Data{
        private int r;
        private int c;
        private int m;
        private int s;
        private int d;
        public Data(int r, int c, int m, int s, int d){
            this.r = r;
            this.c = c;
            this.m = m;
            this.s = s;
            this.d = d;
        }
    }
}
