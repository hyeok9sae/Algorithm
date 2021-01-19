import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_10799 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String s = br.readLine();
		Stack st = new Stack(s.length());
		char b = 0;
		int ans = 0;
		
		for (int i = 0; i < s.length(); i++) {
			if (i != 0) {
				b = s.charAt(i-1);
			}
			char c = s.charAt(i);
			if(c == '(') {
				st.push(c);
			} else {
				if (b == '(') {
					st.pop();
					ans += st.size();
				} else {
					st.pop();
					ans++;
				}
			}
		}
		
		bw.write(ans+"");
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
 *	etc #10799 
 * 	http://boj.kr/10799
 */