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
		Deque dq = new Deque(N);
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String msg = st.nextToken();
			if (msg.equals("push_front")) {
				int num = Integer.parseInt(st.nextToken());
				dq.pushFront(num);
			} else if (msg.equals("push_back")) {
				int num = Integer.parseInt(st.nextToken());
				dq.pushBack(num);
			} else if (msg.equals("pop_front")) {
				bw.write(dq.popFront()+"\n");
			} else if (msg.equals("pop_back")) {
				bw.write(dq.popBack()+"\n");
			} else if (msg.equals("size")) {
				bw.write(dq.size()+"\n");
			} else if (msg.equals("empty")) {
				bw.write(dq.empty()+"\n");
			} else if (msg.equals("front")) {
				bw.write(dq.front()+"\n");
			} else if (msg.equals("back")) {
				bw.write(dq.back()+"\n");
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}
	public static class Deque {
		int[] arr;
//		int front = -1;
		int back = -1;
		
		public Deque(int num) {
			this.arr = new int[num];
		}

		public void pushFront(int num) {
			for (int i = 0; i <= back; i++) {
				arr[back+1-i] = arr[back-i];
			}
			arr[0] = num;
			back++;
		}
		
		public void pushBack(int num) {
			arr[back+1] = num;
			back++;
		}
		
		public int popFront() {
			if (back == -1) {
				return -1;
			}
			int res = arr[0];
			for (int i = 0; i < back; i++) {
				arr[i] = arr[i+1];
			}
			back--;
			return res;
		}
		
		public int popBack() {
			if (back == -1) {
				return -1;
			}
			int res = arr[back];
			back--;
			return res;
		}
		
		public int size() {
			return back+1;
		}
		
		public int empty() {
			if (back == -1) {
				return 1;
			}
			return 0;
		}
		
		public int front() {
			if (back == -1) {
				return -1;
			}
			return arr[0];
		}
		
		public int back() {
			if (back == -1) {
				return -1;
			}
			return arr[back];
		}
	}
}
/*
 *	etc #10866 
 * 	http://boj.kr/10866
 */