import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main_10989 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] list = new int[N];
		
		for (int i = 0; i < N; i++) {
			list[i] = Integer.parseInt(br.readLine());
		}
		
		br.close();
		
		Arrays.sort(list);
		
		for (int i = 0; i < N; i++) {
			bw.write(list[i]+"\n");
		}
		
		bw.flush();
		bw.close();
	}
}
/*
 *	etc #10989 
 * 	http://boj.kr/10989
 */