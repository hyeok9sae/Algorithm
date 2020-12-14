import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main_1158 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int cnt = 0;
		LinkedList<Integer> list = new LinkedList<>();
		ListIterator<Integer> iter = list.listIterator();
		for (int i = 0; i < N; i++) {
			iter.add(i+1);
		}
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		while (list.size() != 0) {
			for (int i = 0; i < K; i++) {
				if(iter.hasNext()) {
					if(i == K-1) {
						sb.append(iter.next());
						if(cnt != N-1) {
							sb.append(", ");
							cnt++;
						}
						iter.remove();
						
					}
					else {
						iter.next();
					}
				} else {
					while(iter.hasPrevious()) {
						iter.previous();
					}
					if(i == K-1) {
						sb.append(iter.next());
						if(cnt != N-1) {
							sb.append(", ");
							cnt++;
						}
						iter.remove();
					}
					else {
						iter.next();
					}
				}
			}
			
		}
		
		sb.append(">");
		bw.write(sb+"");
		br.close();
		bw.flush();
		bw.close();
	}
}
/*
 * etc #1158
 * http://boj.kr/1158
 */