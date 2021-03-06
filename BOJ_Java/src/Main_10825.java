import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main_10825 {
	static ArrayList<Data> list;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		list = new ArrayList<>();
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			list.add(new Data(st.nextToken(), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		br.close();
		
//		for (int i = 0; i < N; i++) {
//			bw.write(list.get(i).name+" "+list.get(i).kor+" "+list.get(i).eng+" "+list.get(i).mat+" "+ "\n");
//		}
//		bw.write("------------------------");
		
		Collections.sort(list, new Comparator<Data>() {
			@Override
			public int compare(Data a, Data b) {
				if (a.kor > b.kor) {
					return -1;
				} else if (a.kor == b.kor) {
					if (a.eng == b.eng) {
						if (a.mat == b.mat) {
							return a.name.compareTo(b.name);
						}
						return Integer.compare(Integer.valueOf(b.mat), Integer.valueOf(a.mat));
					}
					return Integer.compare(Integer.valueOf(a.eng), Integer.valueOf(b.eng));
				} else {
					return 1;
				}
			}
		});
		
		for (int i = 0; i < N; i++) {
			bw.write(list.get(i).name+"\n");
		}
		bw.flush();
		bw.close();
	}
	public static class Data {
		private String name;
		private int kor;
		private int eng;
		private int mat;
		public Data(String name, int kor, int eng, int mat) {
			this.name = name;
			this.kor = kor;
			this.eng = eng;
			this.mat = mat;
		}
//		@Override
//		public String toString() {
//			return name + " " + kor + " " + mat + " " + eng + "\n";
//		}
		
	}
}
/*
 *	etc #10825 
 * 	http://boj.kr/10825
 */
