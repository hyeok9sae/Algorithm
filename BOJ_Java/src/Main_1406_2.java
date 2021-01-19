import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main_1406_2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		String s = br.readLine();
		Editor ed = new Editor(s);
		int M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			if (cmd.equals("L")) {
				ed.L();
			} else if (cmd.equals("D")) {
				ed.D();
			} else if (cmd.equals("B")) {
				ed.B();
			} else if (cmd.equals("P")) {
				char c = st.nextToken().charAt(0);
				ed.P(c);
			}
		}
		bw.write(ed.print()+"");
		
		br.close();
		bw.flush();
		bw.close();
	}
	public static class Editor {
		LinkedList<Character> list;
		ListIterator<Character> iter;
		
		public Editor(String s) {
			list = new LinkedList<>();
			iter = list.listIterator();
			for (int i = 0; i < s.length(); i++) {
				iter.add(s.charAt(i));
			}
		}
		
		public void L() {
			if (iter.hasPrevious()) {
				iter.previous();
			}
		}
		
		public void D() {
			if (iter.hasNext()) {
				iter.next();
			}
		}
		
		public void B() {
			if (iter.hasPrevious()) {
				iter.previous();
				iter.remove();
			}
		}
		
		public void P(char c) {
			iter.add(c);
		}
		
		public StringBuilder print() {
			StringBuilder sb = new StringBuilder();
			for (char c : list) {
				sb.append(c);
			}
			return sb;
		}
	}
}
/*
 * etc #1406
 * http://boj.kr/1406
 */