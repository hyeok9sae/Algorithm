import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_1406 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		String s = br.readLine();
		int M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			if (cmd.equals("L")) {
				
			} else if (cmd.equals("D")) {
				
			} else if (cmd.equals("B")) {
				
			} else if (cmd.equals("P")) {
				String c = st.nextToken();
			}
		}
	}
	public static class Edit {
		int[] arr = new int[600000];
		int cur = 0;
		
		public Edit(int cur) {
			this.cur = cur;
		}
		
		public void add(String s) {
			
		}
		
	}
}
/*
 * etc #1406
 * http://boj.kr/1406
 */
