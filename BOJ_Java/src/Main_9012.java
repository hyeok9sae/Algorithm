import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_9012 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			String s = br.readLine();
			Stack st = new Stack(s.length());
			for (int i = 0; i < s.length(); i++) {
				char c = s.charAt(i);
				if (c == '(') {
					st.push(c);
				} else if (c == ')') {
					if (st.top() == '(') {
						st.pop();
					} else {
						st.push(c);
					}
				}
			}
			if (st.empty() == 1) {
				bw.write("YES\n");
			} else {
				bw.write("NO\n");
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}
	public static class Stack {
		char[] arr;
		int top = -1;
		
		public Stack(int num) {
			this.arr = new char[num];
		}

		public void push(char brk) {
			arr[top+1] = brk;
			top++;
		}
		
		public char pop() {
			if (top == -1) {
				return 'n';
			}
			char res = arr[top];
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
		
		public char top() {
			if (top == -1) {
				return 'n';
			}
			return arr[top];
		}
	}
}
/*
 * etc #9012 
 * http://boj.kr/9012
 */