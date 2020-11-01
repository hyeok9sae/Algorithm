import java.util.Scanner;

public class Main_10818 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		int max = arr[0];
		int min = arr[0];
		for (int i = 0; i < N; i++) {
			if(max < arr[i]) {
				max = arr[i];
			}
			if(min > arr[i]) {
				min = arr[i];
			}
		}
		System.out.println(min+" "+max);
	}
}
/*
 * 입출력 #10818
 * http://boj.kr/10818
 */