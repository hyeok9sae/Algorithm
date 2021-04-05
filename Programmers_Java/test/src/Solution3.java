import java.util.LinkedList;
import java.util.Queue;

public class Solution3 {
    static int[][] map;
    static boolean[][] visited;
    public static void main(String[] args) {
        solution(6, new int[]{1,1,1,1,1,1}, new int[][]{{1,2},{1,3},{1,4},{3,5},{3,6}});
    }
    public static int[] solution(int n, int[] passenger, int[][] train){
        int[] answer = {};
        map = new int[n+1][n+1];
        visited = new boolean[n+1][n+1];
        for (int i = 0; i < train.length; i++){
            map[train[i][0]][train[i][1]] = 1;
            map[train[i][1]][train[i][0]] = 1;
        }
        for (int i = 0; i < n+1; i++){
            for(int j = 0; j < n+1; j++){
                if(visited[i][j] == false){
                    bfs(i, j);
                }
            }
        }
        return answer;
    }
    public static void bfs(int i, int j){
        Queue<int[]> que = new LinkedList<>();
    }

}
