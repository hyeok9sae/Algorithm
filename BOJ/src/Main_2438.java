import java.util.Scanner;

public class Main_2438 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < i+1; j++) {
				System.out.print('*');
			}System.out.println();
		}
	}
}
/*
 *	입출력 #2438 
 * 	http://boj.kr/2438
 */

