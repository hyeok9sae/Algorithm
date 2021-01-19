import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_2609 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		bw.write(gcd(Math.max(num1, num2), Math.min(num1, num2))+"\n");
		bw.write(lcm(num1, num2, gcd(Math.max(num1, num2), Math.min(num1, num2)))+"");
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static int gcd(int num1, int num2) {
		while(num2 > 0) {
			if (num1%num2 == 0) {
				return num2;
			}
			int tmp = num1;
			num1 = num2;
			num2 = tmp%num2;
		}
		return 0;
	}
	
	public static int lcm(int num1, int num2, int gcdNum) {
		
		return (num1*num2)/gcdNum;
	}
}
/*
 * etc #2609 
 * http://boj.kr/2609
 */