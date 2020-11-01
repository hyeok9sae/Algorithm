import java.util.Scanner;

public class Main_8393 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int res = 0;
		for (int i = 0; i < n; i++) {
			res += i+1;
		}
		System.out.println(res);
	}
}
/*
 *	입출력 #8393 
 * 	http://boj.kr/8393
 */