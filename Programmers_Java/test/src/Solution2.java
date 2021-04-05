import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution2 {
    static List<int[]> lst = new ArrayList<>();
    public static void main(String[] args) {
        solution(new int[][]{{1,0,0},{1,1,0},{1,1,0},{1,0,1},{1,1,0},{0,1,1}}, 2);
    }
    public static int solution(int[][] needs, int r){
        int answer = 0;
        int[] arr = new int[needs[0].length];
        combination(arr, 0, arr.length, r);
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < lst.size(); i++){
            int cnt = 0;
            int[] tmp = lst.get(i);
            for (int[] needTmp : needs){
                for (int j = 0; j < needTmp.length; j++){
                    if (needTmp[j] == 1 && tmp[j] == 0){
                        cnt++;
                        break;
                    }
                }
            }
            if (min > cnt){
                min = cnt;
            }
        }
        answer = needs.length-min;

        return answer;
    }
    public static void combination(int[] arr, int start, int n, int r) {
        if(r == 0) {
            int[] tmp = new int[arr.length];
            for (int i = 0; i < arr.length; i++){
                tmp[i] = arr[i];
            }
            lst.add(tmp);
            return;
        }

        for(int i=start; i<n; i++) {
            arr[i] = 1;
            combination(arr, i + 1, n, r - 1);
            arr[i] = 0;
        }
    }
}
