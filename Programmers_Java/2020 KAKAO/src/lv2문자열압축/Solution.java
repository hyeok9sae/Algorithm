package lv2문자열압축;

import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) {
        String s = "abcabcabcabcdededededede";
        int answer = solution(s);
    }
    public static int solution(String s){
        int answer = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 1; i <= s.length()+1/2; i++){
            int j = 0;
//            String[] tmp = new String[(s.length()+1)/2];
            ArrayList<String> tmp = new ArrayList<>();
//            int pn = 0;
            while (true){
                if (j+i > s.length()){
                    tmp.add(s.substring(j, s.length()));
                    break;
                }
//                tmp[pn++] = s.substring(j, j+i);
                tmp.add(s.substring(j, j+i));
                j+=i;
            }
//            System.out.println(tmp+"-");
            int t = 1;
            int cnt = 1;
            String res = "";
            while (true){
                if(tmp.size() < t){
                    break;
                }
                if(t < tmp.size() && tmp.get(t).equals(tmp.get(t-1))){
                    cnt++;
                } else {
                    if(cnt > 1){
                        res += cnt;
                    }
//                    res += cnt;
                    res += tmp.get(t-1);
//                    System.out.println(res);

                    cnt = 1;
                }
                t+= 1;
            }
//            System.out.println(res);
            if (min > res.length()){
                min = res.length();

            }
        }
        System.out.println(min);
        answer = min;
        return answer;
    }
}
