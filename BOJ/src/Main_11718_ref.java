import java.util.Scanner;

public class Main_11718_ref {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextLine()) {
			String s = sc.nextLine();
			System.out.println(s);
		}
	}
}

/*
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class Main_11718 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		while(true) {
			String C = br.readLine();
			if(C == null || C.equals("")) {
				break;
			}
			bw.write(C+"\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
*/
/*
 * 입출력 #11718
 * http://boj.kr/11718
 */