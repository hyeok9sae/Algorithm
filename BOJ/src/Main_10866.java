import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_10866 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String msg = st.nextToken();
			if (msg.equals("push_front")) {
				int num = Integer.parseInt(st.nextToken());
			} else if (msg.equals("push_back")) {
				int num = Integer.parseInt(st.nextToken());
			} else if (msg.equals("pop_front")) {
				
			} else if (msg.equals("pop_back")) {
				
			} else if (msg.equals("size")) {
				
			} else if (msg.equals("empty")) {
				
			} else if (msg.equals("front")) {
				
			} else if (msg.equals("back")) {
				
			}
		}
	}
	public static class Deque {
		ArrayList<Integer> list;
		int front = -1;
		int back = -1;
		
		public void pushFront(int num) {
			
		}
	}
}
/*
 *	etc #10866 
 * 	http://boj.kr/10866
 */