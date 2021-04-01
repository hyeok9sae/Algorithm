package lv1실패율;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        int N = 5;
        int[] stages = {4,4,4,4,4};
        int[] answer = solution(N, stages);
    }
    public static int[] solution(int N, int[] stages){
        int[] answer = {};
        HashMap<Integer, Float> map = new HashMap<>();
        int size = stages.length;
        int clr = size;
        for (int i = 1; i <= N; i++){
            int cnt = 0;
            for (int j = 0; j < size; j++){
                if(stages[j] == i){
//                    System.out.println(i);
                    cnt++;
                }
            }
            float fail = (float)cnt/clr;
            if (cnt == 0){
                fail = 0;
            }
            clr -= cnt;
            map.put(i, fail);
        }
        List<Integer> lst = new ArrayList<>(map.keySet());
        Collections.sort(lst, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
//        System.out.println(map);
//        System.out.println(lst);

        answer = lst.stream().mapToInt(i->i).toArray();
        System.out.println(answer);
        return answer;
    }
}
