package lv2괄호변환;

import java.util.Stack;

public class Solution {
    public static void main(String[] args) {
        String p = "()))((()";
        String answer = solution(p);
    }
    public static String solution(String p){
        String answer = "";
        if (p.equals("")){
            return answer;
        }
        if (prop(p)){
            return p;
        }
        answer += div(p);
        return answer;
    }
    public static String div(String p){
        char s= p.charAt(0);
        int cnt = 1;
        int idx = 0;
        for (int i = 1; i < p.length(); i++){
            if (s == p.charAt(i)){
                cnt++;
            } else {
                cnt--;
            }
            if (cnt == 0){
                idx = i+1;
                break;
            }
        }
        String u = p.substring(0, idx);
        String v;
        if(idx == p.length()){
            v = "";
        } else{
            v = p.substring(idx, p.length());
        }
        if (prop(u)){
            return u += solution(v);
        } else {
            String tmp = "(";
            tmp += solution(v);
            tmp += ")";
            u = u.substring(1, u.length() - 1);
            String cng = "";
            for (int j = 0; j < u.length(); j++){
                if(u.charAt(j) == ')'){
                    cng += '(';
                } else{
                    cng += ')';
                }
            }
            tmp += cng;
            return tmp;
        }
    }
    public static boolean prop(String str){
        Stack<Character> st = new Stack<>();
        if(str.charAt(0) == ')'){
            return false;
        } else{
            st.push(str.charAt(0));
        }
        for (int i = 1; i < str.length(); i++){
            if(st.size() == 0){
                st.push(str.charAt(i));
            }
            else if(st.peek() == ('(')){
                if(str.charAt(i) == ')'){
                    st.pop();
                }else {
                    st.push(str.charAt(i));
                }
            }
        }
        if(st.size() == 0){
            return true;
        } else {
            return false;
        }
    }
}
