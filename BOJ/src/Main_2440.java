import java.util.Scanner;

public class Main_2440 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N - i; j++) {
				System.out.print('*');
			}System.out.println();
		}
	}
}
/*
 *	입출력 #2440 
 * 	http://boj.kr/2440
 */


