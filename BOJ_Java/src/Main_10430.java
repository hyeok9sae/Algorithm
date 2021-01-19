import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10430 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		bw.write((A+B)%C+"\n"+((A%C)+(B%C))%C+"\n"+(A*B)%C+"\n"+((A%C)*(B%C))%C);
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc	#10430
 * http://boj.kr/10430
 */
