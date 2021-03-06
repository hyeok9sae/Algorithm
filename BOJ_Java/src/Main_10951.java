import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10951 {
	public static void main(String[] args) throws Exception {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while(true) {
			String C = br.readLine();
			if(C == null || C.equals("")) {
				break;
			}
			st = new StringTokenizer(C);
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			bw.write(A+B+"\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
/*
 * 입출력 #10951
 * http://boj.kr/10951
 */
