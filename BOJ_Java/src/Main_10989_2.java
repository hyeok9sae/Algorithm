import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_10989_2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[] cnt = new int[10001];
		
		int N = Integer.parseInt(br.readLine());
		
		// 카운팅 정렬
		for (int i = 0; i < N; i++) {
			cnt[Integer.parseInt(br.readLine())]++;
		}
		
		br.close();
		
		for (int i = 1; i <= 10000; i++) {
			while (true) {
				if (cnt[i] == 0) {
					break;
				}
				bw.write(i+"\n");
				cnt[i]--;
			}
		}
		
		bw.flush();
		bw.close();
	}
}
/*
 *	etc #10989 
 * 	http://boj.kr/10989
 */