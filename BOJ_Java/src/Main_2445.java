import java.util.Scanner;

public class Main_2445 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for (int i = 0; i < 2*N-1; i++) {
			if (i <= N-1) {
				for (int j = 0; j < i+1; j++) {
					System.out.print('*');
				}
				for (int j = 0; j < 2*N - (2*i+2); j++) {
					System.out.print(' ');
				}
				for (int j = 0; j < i+1; j++) {
					System.out.print('*');
				}System.out.println();				
			}
			else {
				for (int j = 0; j < 2*N-i-1; j++) {
					System.out.print('*');
				}
				for (int j = 0; j < 2*(i+1-N); j++) {
					System.out.print(' ');
				}
				for (int j = 0; j < 2*N-i-1; j++) {
					System.out.print('*');
				}System.out.println();
			}
		}
	}
}
/*
 *	입출력 #2445 
 * 	http://boj.kr/2445
 */
