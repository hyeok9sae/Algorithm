import java.util.Scanner;

public class Main_1463_ref {
	static int[] dp;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		dp = new int[N+1];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = -1;
		}
		System.out.println(solve(N));
	}
	public static int solve(int n) {
		if (n == 1) {
			return 0;
		}
		if (dp[n] != -1) {
			return dp[n];
		}
		int ret = Integer.MAX_VALUE;
		
		if (n % 3 == 0) {
			ret = Math.min(ret, solve(n / 3) + 1);
		}
		if (n % 2 == 0) {
			ret = Math.min(ret, solve(n / 2) + 1);
		}
		
		return dp[n] = Math.min(ret, solve(n - 1) + 1);
	}
}
/*
 * DP #1463
 * http://boj.kr/1463
 */
