import java.util.Scanner;

public class Main_1924 {
	static int[] mon = {0,31,28,31,30,31,30,31,31,30,31,30,31};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int day = 0;
		for (int i = 0; i < x; i++) {
			day += mon[i];
		}
		day += y;
		if (day % 7 == 1) {
			System.out.println("MON");
		}
		else if (day % 7 == 2) {
			System.out.println("TUE");
		}
		else if (day % 7 == 3) {
			System.out.println("WED");
		}
		else if (day % 7 == 4) {
			System.out.println("THU");
		}
		else if (day % 7 == 5) {
			System.out.println("FRI");
		}
		else if (day % 7 == 6) {
			System.out.println("SAT");
		}
		else {
			System.out.println("SUN");
		}
		
	}
}
/*
 *	입출력#1924 
 * 	http://boj.kr/1924
 */