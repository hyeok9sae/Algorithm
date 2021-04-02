package lv2오픈채팅방;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        String[] answer = solution(record);
    }
    public static String[] solution(String[] record){
        String[] answer = {};
        HashMap<String, String> hm = new HashMap<>();
        HashMap<String, String> hm2 = new HashMap<>();
        List<String> lst = new ArrayList<>();
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < record.length; i++) {
            String[] tmp = record[i].split(" ");
            if (tmp[0].equals("Enter")) {
                hm.put(tmp[0], "님이 들어왔습니다.");
                hm2.put(tmp[1], tmp[2]);
                lst.add(tmp[1] + " " + hm.get(tmp[0]));
            } else if (tmp[0].equals("Leave")) {
                hm.put(tmp[0], "님이 나갔습니다.");
                lst.add(tmp[1] + " " + hm.get(tmp[0]));
            } else if (tmp[0].equals("Change")) {
                hm2.replace(tmp[1], tmp[2]);
            }
        }
        for (String s : lst){
            String[] ss = s.split(" ");
            ans.add(hm2.get(ss[0])+ss[1]+" "+ss[2]);
        }
        answer = new String[ans.size()];
        ans.toArray(answer);
//        for (String i : answer){
//            System.out.println(i);
//        }
        return answer;
    }
}