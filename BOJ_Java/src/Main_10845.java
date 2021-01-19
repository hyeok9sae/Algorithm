import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10845 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		Queue q = new Queue(N);
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String msg = st.nextToken();
			if (msg.equals("push")) {
				int num = Integer.parseInt(st.nextToken());
				q.push(num);
			} else if (msg.equals("pop")) {
				bw.write(q.pop()+"\n");
			} else if (msg.equals("size")) {
				bw.write(q.size()+"\n");
			} else if (msg.equals("empty")) {
				bw.write(q.empty()+"\n");
			} else if (msg.equals("front")) {
				bw.write(q.front()+"\n");
			} else if (msg.equals("back")) {
				bw.write(q.back()+"\n");
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}
	public static class Queue {
		int[] arr;
		int front = -1;
		int back = -1;
		
		public Queue(int n) {
			this.arr = new int[n];
		}
		
		public void push(int num) {
			arr[back+1] = num;
			back++;
		}
		
		public int pop() {
			if (back == front) {
				return -1;
			}
			int res = arr[front+1];
			front++;
			return res;
		}
		
		public int size() {
			return back-front;
		}
		
		public int empty() {
			if (back == front) {
				return 1;
			}
			return 0;
		}
		
		public int front() {
			if (back == front) {
				return -1;
			}
			return arr[front+1];
		}
		
		public int back() {
			if (back == front) {
				return -1;
			}
			return arr[back];
		}
	}
}
/*
 *	etc #10845 
 * 	http://boj.kr/10845
 */