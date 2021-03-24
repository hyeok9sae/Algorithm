import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_20056 {
    static int[][] map;
    static Queue<int[]> que;
    static Queue<int[]> chk;
    static int[] dRow = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dCol = {0, 1, 1, 1, 0, -1, -1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        que = new LinkedList<>();
        chk = new LinkedList<>();

        StringTokenizer st2;
        for (int mm = 0; mm < M; mm++){
            st2 = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st2.nextToken())-1;  // row
            int c = Integer.parseInt(st2.nextToken())-1;  // col
            int m = Integer.parseInt(st2.nextToken());  // 질량
            int s = Integer.parseInt(st2.nextToken());  // 속도
            int d = Integer.parseInt(st2.nextToken());  // 이동 칸
            que.offer(new int[]{r, c, m, s, d}); // 0, 1, 2, 3, 4
            map[r][c] = 1;
        }
        for (int kK = 0; kK < K; kK++){
            int[] tmp;
            int nRow, nCol;
            int n = que.size();
            for (int i = 0; i < n; i++){
                tmp = que.poll();
                map[tmp[0]][tmp[1]] -= 1;
                int dist = tmp[3]%N;
                nRow = tmp[0]+dRow[tmp[4]]*dist;
                nCol = tmp[1]+dCol[tmp[4]]*dist;
                if (nRow >= N) {
                    nRow -= N;
                } else if (nRow < 0){
                    nRow += N;
                }
                if (nCol >= N) {
                    nCol -= N;
                } else if (nCol < 0){
                    nCol += N;
                }
//                System.out.println(nRow+" "+nCol);
                map[nRow][nCol] += 1;
                que.offer(new int[]{nRow, nCol, tmp[2], tmp[3], tmp[4]});
            }
//            System.out.println("-");

            int[] tmp2;
            int[] tmp3;



            int chkD;
            int nsSize;
            int flag = 0;
            for (int i = 0; i < N; i++){
                for (int j = 0; j < N; j++){
                    int cnt = 0;
                    int cnt2 = 0;
                    int qSize = que.size();
                    int mSize = map[i][j];
                    if (map[i][j] > 1){
                        while (true){
                            tmp2 = que.poll();
                            map[tmp2[0]][tmp2[1]] -= 1;
                            if (i == tmp2[0] && j == tmp2[1]){
//                                System.out.println(i+" "+j+"d");
                                chk.offer(tmp2);
                                cnt2 += 1;
                                if (mSize == cnt2){
                                    break;
                                }
                            } else {
                                que.offer(tmp2);
                                map[tmp2[0]][tmp2[1]] += 1;
                            }
                            cnt += 1;
                            if (cnt == qSize){
                                break;
                            }
                        }
                        nsSize = chk.size();
                        int tmpD = 0;
                        if (chk.size() != 0){
                            tmpD = isChk(chk.peek()[4]);
                        }
                        int[] chkDigit = new int[nsSize];
                        int pn = 0;
                        int nM = 0;
                        int nS = 0;
                        while (!chk.isEmpty()){
                            tmp3 = chk.poll();
                            nM += tmp3[2];
                            nS += tmp3[3];
                            chkD = tmp3[4];
                            chkDigit[pn++] = chkD;
                        }
                        int t = 1;
                        while (t < nsSize){
                            if (tmpD == 0){
                                if (chkDigit[t] % 2 == 1){
                                    flag = 1;
                                    break;
                                }
                            } else {
                                if (chkDigit[t] % 2 == 0){
                                    flag = 1;
                                    break;
                                }
                            }
                            t += 1;
                        }
                        if (flag == 0){
                            for (int nD = 0; nD < 8; nD+=2){
                                if (nM/5 == 0){
                                    break;
                                }
                                que.offer(new int[]{i, j, nM/5, nS/nsSize, nD});
                                map[i][j] += 1;
                            }
                        } else{
                            for (int nD = 1; nD < 8; nD+=2){
                                if (nM/5 == 0){
                                    break;
                                }
//                                System.out.println(i+" "+j+" "+nM/5+" "+nS/nsSize+" "+nD+" ");
                                que.offer(new int[]{i, j, nM/5, nS/nsSize, nD});
                                map[i][j] += 1;
                            }
                        }
                    }
                }
            }
        }
        int answer = 0;
        while (!que.isEmpty()){
            answer += que.poll()[2];
        }
        bw.write(answer+"");
        br.close();
        bw.flush();
        bw.close();
    }
    public static int isChk(int num){
        if (num % 2 == 0){
            return 0;
        } else{
            return 1;
        }
    }
}