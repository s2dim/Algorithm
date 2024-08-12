import java.util.*;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		char [] charArr = str.toCharArray();
		int len = charArr.length;
		
		int r = 0;
		int c = 1;
		
		for (int i = 1; i <= len / 2; i++) {
			if (i > c) {
				break;
			}
			if (len % i == 0 && i <= len / i) {
				r = i;
				c = len / i;
			}
		}
		
		char[][] arr = new char[r][c];
		
		int idx = 0;
		for (int i = 0; i < c; i++) {
			for (int j = 0; j < r; j++) {
				arr[j][i] = charArr[idx];
				idx++;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				sb.append(arr[i][j]);
			}
		}
		System.out.println(sb);
	}
}
