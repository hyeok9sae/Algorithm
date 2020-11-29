import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_10814 {
	static int[] age;
	static String[] name;
	static int[] tmpAge;
	static String[] tmpName;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		age = new int[N];
		tmpAge = new int[age.length];
		name = new String[age.length];
		tmpName = new String[age.length];
		for (int i = 0; i < age.length; i++) {
			st = new StringTokenizer(br.readLine());
			age[i] = Integer.parseInt(st.nextToken());
			name[i] = st.nextToken();
		}
		br.close();
		mergeSort(0, age.length-1);
		for (int i = 0; i < age.length; i++) {
			bw.write(age[i] + " " + name[i] + "\n");
		}
		bw.flush();
		bw.close();
	}
	public static void mergeSort(int start, int end) {
		if (start < end) {
			int mid = (start + end) / 2;
			mergeSort(start, mid);
			mergeSort(mid + 1, end);
			merge(start, mid, end);
		}
	}
	public static void merge(int start, int mid, int end) {
		int i = start;
		int j = mid + 1;
		int k = i;
		
		while (i <= mid && j <= end) {
			if (age[i] < age[j]) {
				tmpAge[k] = age[i];
				tmpName[k++] = name[i++];
			} else if (age[i] == age[j]) {
				if (i < j) {
					tmpAge[k] = age[i];
					tmpName[k++] = name[i++];
				} else {
					tmpAge[k] = age[j];
					tmpName[k++] = name[j++];
				}
			} else {
				tmpAge[k] = age[j];
				tmpName[k++] = name[j++];
			}
		}
		
		while (i <= mid) {
			tmpAge[k] = age[i];
			tmpName[k++] = name[i++];
		}
		
		while (j <= end) {
			tmpAge[k] = age[j];
			tmpName[k++] = name[j++];
		}
		
		for (int t = start; t <= end; t++) {
			age[t] = tmpAge[t];
			name[t] = tmpName[t];
		}
	}
}
/*
 * etc #10814
 * http://boj.kr/10814
 */
