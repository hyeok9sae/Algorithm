import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_10808 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		int[] alp = new int[26];
		for (int i = 0; i < s.length(); i++) {
			alp[s.charAt(i)-97]++;
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
 * etc #10808
 * http://boj.kr/10808
 */
