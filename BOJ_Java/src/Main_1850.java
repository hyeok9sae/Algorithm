import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_1850 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		long A = Long.parseLong(st.nextToken());
		long B = Long.parseLong(st.nextToken());
		long res = gcd(Math.max(A, B), Math.min(A, B));
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < res; i++) {
			sb.append("1");
		}
		bw.write(sb+"");
		
		br.close();
		bw.flush();
		bw.close();
	}
	public static long gcd(long num1, long num2) {
		while (num2 > 0) {
			long tmp = num1;
			num1 = num2;
			num2 = tmp%num2;
		}
		return num1;
	}
}
/*
 *	etc #1850 
 * 	http://boj.kr/1850
 */