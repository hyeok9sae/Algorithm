import java.util.HashSet;
import java.util.Iterator;

public class Solution {
    public static void main(String[] args) {
        solution(new int[]{5,4,5,4,5}, new int[]{1,2,3,5,4});
    }
    public static int solution(int[] gift_cards, int[] wants){
        int answer = 0;
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();

        for (int i : gift_cards){
            set1.add(i);
        }
        for (int i : wants){
            set2.add(i);
        }
        int[] arr = new int[set1.size()];
        int[] arr2 = new int[set2.size()];
        Iterator<Integer> iter = set1.iterator();
        Iterator<Integer> iter2 = set2.iterator();
        int pn = 0;
        while (iter.hasNext()){
            arr[pn++] = iter.next();
        }
        pn = 0;
        while (iter2.hasNext()){
            arr2[pn++] = iter2.next();
        }
        int cnt = 0;
        int cnt2 = 0;
        if (arr.length >= arr2.length){
            for (int i = 0; i < arr.length; i++){
                for (int j = 0; j < arr2.length; j++){
                    if (arr[i] == arr2[j]){
                        cnt++;
                        break;
                    }
                }
            }
            answer = arr.length-cnt;
        } else{
            for (int i = 0; i < arr2.length; i++){
                for (int j = 0; j < arr.length; j++){
                    if (arr2[i] == arr[j]){
                        cnt2++;
                        break;
                    }
                }
            }
            answer = arr2.length-cnt2;
        }
        return answer;
    }
}