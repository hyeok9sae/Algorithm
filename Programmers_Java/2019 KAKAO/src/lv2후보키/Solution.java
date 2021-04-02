package lv2후보키;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Solution {
    static HashSet<Integer> hs;

    public static void main(String[] args) {
        hs = new HashSet<>();
        for (int i = 0; i < 5; i++){
            hs.add(i);
        }
        hs.add(6);
        hs.add(3);
        System.out.println(hs);
    }
}
