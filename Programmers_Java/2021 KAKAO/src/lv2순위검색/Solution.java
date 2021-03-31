package lv2순위검색;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        String[] info = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
        String[] query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
        int[] answer = solution(info, query);
    }
    public static int[] solution(String[] info, String[] query){
        int[] answer = new int[query.length];
//        Queue<String[]> que = new LinkedList<>();
        ArrayList<String[]> lst = new ArrayList<>();
        for (int i = 0; i < info.length; i++){
            String[] app = info[i].split(" ");
            lst.add(app);
        }
//        System.out.println(lst.get(0)[0]+" "+lst.get(0)[4]);
        Collections.sort(lst, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if (Integer.parseInt(o1[4]) < Integer.parseInt(o2[4])){
                    return 1;
                }
                if (Integer.parseInt(o1[4]) > Integer.parseInt(o2[4])){
                    return -1;
                }
                return 0;
            }
        });
//        System.out.println(lst.get(0)[0]+" "+lst.get(0)[4]);
//        int qSize = que.size();
        int qSize = lst.size();
        for (int i = 0; i < query.length; i++){
            int cnt = 0;
            String[] req = new String[5];
            StringTokenizer st = new StringTokenizer(query[i]);
            int k = 0;
            while (k < 5){
                String str = st.nextToken();
                if (str.equals("and")){
                    continue;
                }
                req[k] = str;
                k++;
            }

            for (int j = 0; j < qSize; j++){
                String[] tmp = lst.get(j);
                if (Integer.parseInt(tmp[4]) < Integer.parseInt(req[4])){
                    break;
                }
                if (!req[0].equals("-")){
                    if (!tmp[0].equals(req[0])){
                        continue;
                    }
                }
                if (!req[1].equals("-")){
                    if (!tmp[1].equals(req[1])){
                        continue;
                    }
                }
                if (!req[2].equals("-")){
                    if (!tmp[2].equals(req[2])){
                        continue;
                    }
                }
                if (!req[3].equals("-")){
                    if (!tmp[3].equals(req[3])){
                        continue;
                    }
                }

                cnt++;
            }
            answer[i] = cnt;
        }
        for (int i = 0; i < answer.length; i++){
            System.out.print(answer[i]+" ");
        }
        return answer;
    }
}
