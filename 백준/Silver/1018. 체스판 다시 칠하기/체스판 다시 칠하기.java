
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		char[][] arr = new char[n][m];
		char[][] black = new char[8][8];
		char[][] white = new char[8][8];
		

		// 배열 생성
		for (int i = 0; i < n; i++) {
			String str = sc.next();
//			sc.nextLine();
			arr[i] = str.toCharArray();
		}
		
		char[] line1 = {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'};
		char[] line2 = {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'};
		
		// 검정 시작 체스판
		for (int i = 0; i < 8; i = i + 2) {
			black[i] = line2;
			black[i+1] = line1;
			white[i] = line1;
			white[i+1] = line2;
		}
		

		int min = Integer.MAX_VALUE;
		
		for (int i = 0; i <= n - 8; i++) {
			for (int j = 0; j <= m - 8; j++) {
				
				int sum = 0;
				int sum2 = 0;

				for (int x = i; x < i + 8; x++) {
					for (int y = j; y < j + 8; y++) {
						if (arr[x][y] != black[x-i][y-j])
							sum++;
						if (arr[x][y] != white[x-i][y-j])
							sum2++;

					}


				}
				min = Math.min(min, Math.min(sum, sum2));

			}
		}

		System.out.println(min);

	}
}
