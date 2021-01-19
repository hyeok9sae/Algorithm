import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_11655 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
				bw.write(((s.charAt(i)-'A'+13) % 26)+'A');
			} else if (s.charAt(i) >= 'a' && s.charAt(i) <= 'z') {
				bw.write(((s.charAt(i)-'a'+13) % 26)+'a');
			} else {
				bw.write(s.charAt(i));
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc #11655
 * http://boj.kr/11655
 */
