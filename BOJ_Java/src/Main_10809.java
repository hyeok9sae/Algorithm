import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main_10809 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		
		int[] alp = new int[26];
		
		Arrays.fill(alp, -1);
		
		for (int i = 0; i < s.length(); i++) {
			if(alp[s.charAt(i)-97] != -1 && alp[s.charAt(i)-97] < i) {
				continue;
			}
			alp[s.charAt(i)-97] = i;
		}
		
		for (int i = 0; i < alp.length; i++) {
			bw.write(alp[i]+" ");
		}
		
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc #10809 
 * http://boj.kr/10809
 */