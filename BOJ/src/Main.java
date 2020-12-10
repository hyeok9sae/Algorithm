import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 
        String s = "";
 
        while ((s = br.readLine()) != null ) {
 
            int[] arr = new int[4];
 
            for (int i = 0; i < s.length(); i++) {
            	char c = s.charAt(i);
                // 소문자
            	if ((int)c >= 97 && (int)c <= 122) {
					arr[0]++;
				}  if ((int)c >= 65 && (int)c <= 90) {
					arr[1]++;
				}  if ((int)c >= 48 && (int)c <= 57) {
					arr[2]++;
				}  if ((int)c == 32) {
					arr[3]++;
				}
 
            }
 
            bw.write(arr[0]+" "+arr[1]+" "+arr[2]+" "+arr[3]+"\n");
            
            bw.flush();
        }
        br.close();
        bw.close();
    }
 
}