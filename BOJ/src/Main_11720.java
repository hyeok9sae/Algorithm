import java.util.Scanner;

public class Main_11720 {
	static char[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String s = sc.next();
		int res = 0;
		char[] arr = new char[num];
		for (int i = 0; i < num; i++) {
			arr[i] = s.charAt(i);
			res += Integer.parseInt(String.valueOf(arr[i]));
		}
		System.out.println(res);
	}
}
/*
 *	ÀÔÃâ·Â #11720 
 *  http://boj.kr/11720
 */
