import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_1934 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
			int ans = (num1*num2)/gcd(Math.max(num1, num2), Math.min(num1, num2));
			sb.append(ans+"\n");
		}
		bw.write(sb+"");
		br.close();
		bw.flush();
		bw.close();
	}
	public static int gcd(int num1, int num2) {
		while (num2 > 0) {
			if (num1 % num2 == 0) { //어차피 나누어떨어지면 0이므로 이 if문은 없어도 되는 구문
				return num2;
			}
			int tmp = num1;
			num1 = num2;
			num2 = tmp%num2;
		}
		return 0;
	}
}
/*
 * etc #1934
 * http://boj.kr/1934
 */
