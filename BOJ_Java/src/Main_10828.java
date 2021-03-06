import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10828 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		String msg;
		int num;
		
		Stack stack = new Stack(N);
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			msg = st.nextToken();
			
			if (msg.equals("push")) {
				num = Integer.parseInt(st.nextToken());
//				bw.write(msg+" "+num+"\n");
				stack.push(num);
			} else if (msg.equals("pop")) {
//				bw.write(msg+"\n");
				bw.write(stack.pop()+"\n");
			} else if (msg.equals("size")) {
//				bw.write(msg+"\n");
				bw.write(stack.size()+"\n");
			} else if (msg.equals("empty")) {
//				bw.write(msg+"\n");
				bw.write(stack.empty()+"\n");
			} else if (msg.equals("top")) {
//				bw.write(msg+"\n");
				bw.write(stack.top()+"\n");
			}
		}
		
		br.close();
		bw.flush();
		bw.close();
		
	}
	public static class Stack {
		int[] arr;
		int top = -1;
		
		public Stack(int num) {
			this.arr = new int[num];
		}
		
		public void push(int num) {
			arr[top+1] = num;
			top++;
		}
		
		public int pop() {
			if (top == -1) {
				return -1;
			}
			int res = arr[top];
			top--;
			return res;
		}
		
		public int size() {
			return top+1;
		}
		
		public int empty() {
			if (top == -1) {
				return 1;
			}
			return 0;
		}
		
		public int top() {
			if (top == -1) {
				return -1;
			}
			return arr[top];
		}
	}
}
/*
 * etc	#10828
 * http://boj.kr/10828
 */
