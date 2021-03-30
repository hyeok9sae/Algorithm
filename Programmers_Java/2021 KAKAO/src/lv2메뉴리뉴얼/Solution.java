package lv2메뉴리뉴얼;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2,3,4};
        String[] answer = solution(orders, course);
    }
    static HashMap<String, Integer> map = new HashMap<>();

    public static String[] solution(String[] orders, int[] course){
        String[] answer = {};
        for (int i = 0; i < orders.length; i++){
            char[] tmp = orders[i].toCharArray();
            Arrays.sort(tmp);
            boolean[] visited = new boolean[tmp.length];
            for (int j = 0; j < course.length; j++){
                comb(tmp, visited, 0, course[j]);
            }
        }
        List<String> keySetList = new ArrayList<>(map.keySet());
        Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
        List<String> ansList = new ArrayList<>();
        for (int i = 0; i < course.length; i++){
            int max = 0;
            for (String s : keySetList){
                if(s.length() == course[i] && map.get(s) >= 2){
                    if (max <= map.get(s)){
                        max = map.get(s);
                        ansList.add(s);
                    }
                }
            }
        }
        Collections.sort(ansList);
//        System.out.println(ansList);
        answer = new String[ansList.size()];
        ansList.toArray(answer);
        return answer;
    }
    public static void comb(char[] tmp, boolean[] visited, int start, int r){
        if (r == 0){
            String tmpKey = "";
            for (int i = 0; i < tmp.length; i++){
                if (visited[i] == true){
//                    System.out.print(tmp[i]+" ");
                    tmpKey += tmp[i];
                }
            }
            map.put(tmpKey, map.getOrDefault(tmpKey, 0) + 1);
//            System.out.println();
            return;
        }
        for (int i = start; i < tmp.length; i++){
            visited[i] = true;
            comb(tmp, visited,i+1, r-1);
            visited[i] = false;
        }

    }
}
