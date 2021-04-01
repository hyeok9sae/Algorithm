package lv2후보키;

public class Solution {
    public static void main(String[] args) {
        String[][] relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
        int answer = solution(relation);
    }
    public static int solution(String[][] relation){
        int answer = 0;
        int attSize = relation[0].length;
        int[] arr = new int[attSize];
        for (int i = 0; i < attSize; i++){
            arr[i] = i;
        }
        boolean[] visited = new boolean[attSize];
        for (int r = 0; r < arr.length-1; r++){
            comb(arr, visited);
        }
        return answer;
    }
    public static void
}
