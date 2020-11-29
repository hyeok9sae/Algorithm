import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_11650 {
	static int[][] arr;
	static int[][] tmp;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		arr = new int[N][2];
		tmp = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 2; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		br.close();
		mergeSort(0, N-1);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 2; j++) {
				bw.write(arr[i][j]+" ");
			}bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
	public static void mergeSort(int start, int end) {
		if (start < end) {
			int mid = (start + end) / 2;
			mergeSort(start, mid);
			mergeSort(mid+1, end);
			merge(start, mid, end);
		}
	}
	public static void merge(int start, int mid, int end) {
		int i = start;
		int j = mid + 1;
		int k = i;
		
		while(i <= mid && j <= end) {
			if (arr[i][0] < arr[j][0]) {
				tmp[k][0] = arr[i][0];
				tmp[k++][1] = arr[i++][1];
			} else if (arr[i][0] == arr[j][0]) {
				if (arr[i][1] <= arr[j][1]) {
					tmp[k][0] = arr[i][0];
					tmp[k++][1] = arr[i++][1];
				} else {
					tmp[k][0] = arr[j][0];
					tmp[k++][1] = arr[j++][1];
				}
			} else {
				tmp[k][0] = arr[j][0];
				tmp[k++][1] = arr[j++][1];
			}
		}
		while(i <= mid) {
			tmp[k][0] = arr[i][0];
			tmp[k++][1] = arr[i++][1];
		}
		while(j <= end) {
			tmp[k][0] = arr[j][0];
			tmp[k++][1] = arr[j++][1];
		}
		for (int t = start; t <= end; t++) {
			arr[t][0] = tmp[t][0];
			arr[t][1] = tmp[t][1];
		}
	}
}
/*
 *	etc #11650 
 * 	http://boj.kr/11650
 */