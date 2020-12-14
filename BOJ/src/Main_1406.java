import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main_1406 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		LinkedList<Character> list = new LinkedList<>();
		ListIterator<Character> iter = list.listIterator();
		String s = br.readLine();
		for (int i = 0; i < s.length(); i++) {
			iter.add(s.charAt(i));
		}
		int M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			String d = st.nextToken();
			if (d.equals("L")) {
				if (iter.hasPrevious()) {
					iter.previous();
				}
			} else if (d.equals("D")) {
				if (iter.hasNext()) {
					iter.next();
				}
			} else if (d.equals("B")) {
				if (iter.hasPrevious()) {
					iter.previous();
					iter.remove();
				}
			} else if (d.equals("P")) {
				char c = st.nextToken().charAt(0);
				iter.add(c);
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (char a : list) {
			sb.append(a);
		}
		bw.write(sb+"");
		
//		for (int i = 0; i < list.size(); i++) {
//			bw.write(list.get(i));
//		} // 시간초과
		
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc #1406
 * http://boj.kr/1406
 */
