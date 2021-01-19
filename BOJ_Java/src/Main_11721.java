import java.util.Scanner;

public class Main_11721 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		for (int i = 0; i < s.length(); i++) {
			if(i % 10 == 0 && i != 0) {
				System.out.println();
				System.out.print(s.charAt(i));
			} else {
				System.out.print(s.charAt(i));
			}
		}
	}
}
/*
 * 입출력 #11721
 * http://boj.kr/11721
 */