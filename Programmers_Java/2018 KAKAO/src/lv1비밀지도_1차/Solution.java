package lv1비밀지도_1차;

public class Solution {
    public static void main(String[] args) {
        System.out.println(solution(5, new int[]{9, 20, 28, 18, 11}, new int[]{30, 1, 21, 17, 28}));
    }
    public static String[] solution(int n, int[] arr1, int[] arr2){
        String[] answer = new String[n];
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++){
            int num = arr1[i];
            for (int j = n-1; j >= 0; j--){
                if (num/2 == 0){
                    map[i][j] = num%2;
                    break;
                }
                map[i][j] = num%2;
                num /= 2;
            }
        }
        for (int i = 0; i < n; i++){
            int num = arr2[i];
            for (int j = n-1; j >= 0; j--){
                if (map[i][j] == 1){
                    num /= 2;
                    continue;
                }
                if (num/2 == 0){
                    map[i][j] = num%2;
                    break;
                }
                map[i][j] = num%2;
                num /= 2;
            }
        }
        for (int i = 0; i < n; i++){
            String s = "";
            for (int j = 0; j < n; j++){
                if (map[i][j] == 1){
                    s += "#";
                } else {
                    s += " ";
                }
            }
            answer[i] = s;
            System.out.print(s+" ");
        }
        return answer;
    }
}
