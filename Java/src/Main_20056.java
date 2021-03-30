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
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        map = new int[N][N];
        que = new LinkedList<>();
        chk = new LinkedList<>();

        for (int mm = 0; mm < M; mm++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st2.nextToken())-1;
            int c = Integer.parseInt(st2.nextToken())-1;
            int m = Integer.parseInt(st2.nextToken());
            int s = Integer.parseInt(st2.nextToken());
            int d = Integer.parseInt(st2.nextToken());
            que.offer(new int[]{r, c, m, s, d}); // 0, 1, 2, 3, 4
            map[r][c] = 1;
        }

        for (int kk = 0; kk < K; kk++){
            int qSize = que.size();
            for (int q = 0; q < qSize; q++){
                int[] tmp = que.poll();
                map[tmp[0]][tmp[1]] -= 1;
                int dist = tmp[3]%N;
                int nRow = tmp[0]+(dRow[tmp[4]]*dist);
                int nCol = tmp[1]+(dCol[tmp[4]]*dist);
                if (nRow >= N){
                    nRow -= N;
                } else if (nRow < 0){
                    nRow += N;
                }
                if (nCol >= N){
                    nCol -= N;
                } else if (nCol < 0){
                    nCol += N;
                }
                que.offer(new int[]{nRow, nCol, tmp[2], tmp[3], tmp[4]});
                map[nRow][nCol] += 1;
            }
            int ckSize = que.size();
            int cnt = 0;
            for (int i = 0; i < N; i++){
                for (int j = 0; j < N; j++){
                    if (map[i][j] >= 1){
                        cnt += map[i][j];
                    }
                    if (map[i][j] > 1){
                        int cntChk = 0;
                        int mapSize = map[i][j];
                        qSize = que.size();
                        for (int k = 0; k < qSize; k++){
                            int[] tmp2 = que.poll();
                            map[tmp2[0]][tmp2[1]] -= 1;
                            if (tmp2[0] == i && tmp2[1] == j){
                                chk.offer(tmp2);
                                cntChk++;
                                if (cntChk == mapSize){
                                    break;
                                }
                            } else {
                                que.offer(tmp2);
                                map[tmp2[0]][tmp2[1]] += 1;
                            }
                        }
                        int nM = 0;
                        int nS = 0;
                        int cSize = chk.size();
                        int tmpD = chk.peek()[4] % 2;
                        int flag = 0;
                        while (!chk.isEmpty()){
                            int[] tmp3 = chk.poll();
                            nM += tmp3[2];
                            nS += tmp3[3];
                            if (tmp3[4] % 2 != tmpD){
                                flag = 1;
                            }
                        }
                        nM /= 5;
                        if (nM == 0){
                            continue;
                        }
                        nS /= cSize;
                        if (flag == 0){
                            for (int nD = 0; nD < 8; nD+=2){
                                que.offer(new int[]{i, j, nM, nS, nD});
                                map[i][j] += 1;
                            }
                        } else {
                            for (int nD = 1; nD < 8; nD+=2){
                                que.offer(new int[]{i, j, nM, nS, nD});
                                map[i][j] += 1;
                            }
                        }
                    }
                    if (cnt == ckSize){
                        break;
                    }
                }
                if (cnt == ckSize){
                    break;
                }
            }
        }

        int answer = 0;
        while(!que.isEmpty()){
            answer += que.poll()[2];
        }
        bw.write(answer+"");

        br.close();
        bw.flush();
        bw.close();
    }
}
