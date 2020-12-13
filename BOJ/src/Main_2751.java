import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_2751 {
	static int[] arr;
	static int[] tmp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		tmp = new int[arr.length];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		br.close();
		
		mergeSort(0, arr.length-1);
		for (int n = 0; n < arr.length; n++) {
			bw.write(arr[n]+"\n");
		}
		bw.flush();
		bw.close();
	}
	public static void mergeSort(int start, int end) {
		if(start < end) {
			int mid = (start + end)/2;
			mergeSort(start, mid);
			mergeSort(mid+1, end);
			merge(start, mid, end);
		}
	}
	public static void merge(int start, int mid, int end) {
		int i = start;
		int j = mid+1;
		int k = i;
		while (i <= mid && j <= end) {
			if (arr[i] < arr[j]) {
				tmp[k++] = arr[i++];
			} else {
				tmp[k++] = arr[j++];
			}
		}
		while (i <= mid) {
			tmp[k++] = arr[i++];
		}
		while (j <= end) {
			tmp[k++] = arr[j++];
		}
		for (int t = start; t <= end; t++) {
			arr[t] = tmp[t];
		}
	}
}
/*
 * etc #2751
 * http://boj.kr/2751
 */
 