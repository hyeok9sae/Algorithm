package lv1신규아이디추천;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {   // 신규 아이디 추천
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String new_id = br.readLine();
        String s = solution(new_id);
    }
    public static String solution(String new_id){
        String answer = "";
        // 1
        new_id = new_id.toLowerCase();
        System.out.println("1: "+new_id);
        // 2
        String tmp = "";
        for (int i = 0; i < new_id.length(); i++){
            if (('a' <= new_id.charAt(i) && new_id.charAt(i) <= 'z') || ('0' <= new_id.charAt(i) && new_id.charAt(i) <= '9') || new_id.charAt(i) == '.' || new_id.charAt(i) == '-' || new_id.charAt(i) == '_'){
                tmp += new_id.charAt(i);
            }
        }
        new_id = tmp;
        System.out.println("2: "+new_id);
        // 3
        tmp = "";
        tmp += new_id.charAt(0);
        for (int i = 1; i < new_id.length(); i++){
            if (new_id.charAt(i-1) == '.'){
                if (new_id.charAt(i) == '.'){
                    continue;
                }
            }
            tmp += new_id.charAt(i);
        }
        new_id = tmp;
        System.out.println("3: "+new_id);
        // 4
        tmp = "";
        for (int i = 0; i < new_id.length(); i++){
            if ((i == 0 || i == new_id.length()-1) && new_id.charAt(i) == '.'){
                continue;
            }
            tmp += new_id.charAt(i);
        }
        new_id = tmp;
        System.out.println("4: "+new_id);
        // 5
        if (new_id == ""){
            new_id = "a";
        }
        System.out.println("5: "+new_id);
        // 6
        tmp = "";
        if (new_id.length() >= 16){
            for (int i = 0; i < 15; i++){
                if (i == 14 && new_id.charAt(i) == '.'){
                    break;
                }
                tmp += new_id.charAt(i);
            }
            new_id = tmp;
        }
        System.out.println("6: "+new_id);
        // 7
        if (new_id.length() <= 2){
            while (new_id.length() <= 2){
                new_id += new_id.charAt(new_id.length()-1);
            }
        }
        System.out.println("7: "+new_id);
        answer = new_id;
        return answer;
    }
}
