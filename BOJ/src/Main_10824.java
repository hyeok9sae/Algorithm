import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10824 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String A = st.nextToken();
		String B = st.nextToken();
		String C = st.nextToken();
		String D = st.nextToken();
		
		bw.write(Long.parseLong(A+B)+Long.parseLong(C+D)+"");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc #10824 
 * http://boj.kr/10824
 */