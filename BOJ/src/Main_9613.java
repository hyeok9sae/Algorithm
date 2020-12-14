import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_9613 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[] arr = new int[N];
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			long res = 0;
			for (int i = 0; i < N; i++) {
				for (int j = i+1; j < N; j++) {
					res += gcd(Math.max(arr[i], arr[j]), Math.min(arr[i], arr[j]));
				}
			}
			sb.append(res+"\n");
		}
		bw.write(sb+"");
		br.close();
		bw.flush();
		bw.close();
	}
	public static int gcd(int num1, int num2) {
		while (num2 > 0) {
			int tmp = num1;
			num1 = num2;
			num2 = tmp%num2;
		}
		return num1;
	}
}
/*
 *	etc #9613 
 * 	http://boj.kr/9613
 */