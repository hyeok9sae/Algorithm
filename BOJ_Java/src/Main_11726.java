import java.util.Arrays;
import java.util.Scanner;

public class Main_11726 {
	static int[] dp;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		dp = new int[n+1];
		Arrays.fill(dp, -1);
		System.out.println(solve(n));
	}
	public static int solve(int n) {
		if (n == 1) {
			return dp[n] = 1;
		}
		if (n == 2) {
			return dp[n] = solve(1) + 1;
		}
		if (dp[n] != -1) {
			return dp[n];
		}
		return dp[n] = (solve(n-1) + solve(n-2))%10007;
	}
}
/*
 * DP #11726
 * http://boj.kr/11726
 */
