import java.util.Scanner;

public class Main_10953 {
//	static char[] c; 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		StringBuilder sb = new StringBuilder();
//		StringBuilder sbb = new StringBuilder();
		int T = sc.nextInt();
		for (int t = 0; t < T; t++) {
			String s = sc.next();
			String[] arr = s.split(",");
			System.out.println(Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]));
		}
	}
}
/*
 * 입출력#10953
 * http://boj.kr/10953
 */