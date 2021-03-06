import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main_11652 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());

		long[] arr = new long[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(br.readLine());
		}
		
		br.close();
		
		Arrays.sort(arr);
		
		int res = 1;
		int ans = 0;
		long ansNum = 0;
		
		for (int i = 0; i < N-1; i++) {
			if (arr[i] == arr[i+1]) {
				res++;
			} else {
				if (ans < res) {
					ans = res;
					ansNum = arr[i];
				}
				res = 1;
			}
		}
		if (ans < res) {
			ans = res;
			ansNum = arr[N-1];
		}
		bw.write(ansNum+"");
		bw.flush();
		bw.close();
	}
}
/*
 *	etc #11652 
 * 	http://boj.kr/11652
 */

