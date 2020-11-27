import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class Main_2751_2 {
	static int[] tmp;
	public static void main(String[] args) throws IOException {
		ArrayList<Integer> list = new ArrayList<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		tmp = new int[list.size()];
		for (int i = 0; i < N; i++) {
			list.add(Integer.parseInt(br.readLine()));
		}
		br.close();
		Collections.sort(list);
		for (int i = 0; i < N; i++) {
			bw.write(list.get(i)+"\n");
		}
		bw.flush();
		bw.close();
	}
}
