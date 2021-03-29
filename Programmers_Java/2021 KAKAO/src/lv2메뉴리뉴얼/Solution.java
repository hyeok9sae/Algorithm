package lv2메뉴리뉴얼;

import java.util.HashMap;

public class Solution {
    static HashMap<String, Integer> map;
    public static void main(String[] args) {
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2, 3, 4};
        String[] answer = solution(orders, course);
    }
    public static String[] solution(String[] orders, int[] course){
        String[] answer = {};
        map= new HashMap<>();
        for (int i = 0; i < orders.length; i++){
            char[] tmp = new char[orders[i].length()];
            boolean[] visited = new boolean[orders[i].length()];
            for (int j = 0; j < orders[i].length(); j++){
                tmp[j] = orders[i].charAt(j);
            }
            for (int r = 0; r < course.length; r++){
                comb(tmp, visited, 0, course[r], map);
            }
        }
        return answer;
    }
    public static void comb(char[] arr, boolean[] visited, int start, int r, HashMap<String, Integer> map){
        if (r == 0){
            for (int i = 0; i < arr.length; i++){
                if (visited[i] == true){
                    System.out.print(arr[i] + " ");
                }
                System.out.println();
            }
            return;
        } else{
            for (int i = start; i < arr.length; i++){
                visited[i] = true;
                comb(arr, visited, i+1, r-1, map);
                visited[i] = false;
            }
        }
    }
}
