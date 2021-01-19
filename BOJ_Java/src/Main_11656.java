import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main_11656 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		String[] arr = new String[s.length()];
		Arrays.fill(arr, "");
		for (int i = 0; i < s.length(); i++) {
			for (int j = i; j < s.length(); j++) {
				arr[i] += s.charAt(j);
			}
		}
		Arrays.sort(arr);
		for (int i = 0; i < s.length(); i++) {
			bw.write(arr[i]+"\n");
		}
		
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 *	etc #11656 
 * 	http://boj.kr/11656
 */