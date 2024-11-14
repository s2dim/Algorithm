import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[][] arr = new int[n][n];
		int[][] dp = new int[n][n];
		
		// 배열 입력
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i+1; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		dp[0][0] = arr[0][0];
		
		
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < i+1; j++) {
				if (j == 0) {
					dp[i][j] = dp[i-1][j] + arr[i][j];
				} else if (j == i) {
					dp[i][j] = dp[i-1][j-1] + arr[i][j];
				} else {
					dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j];
				}
			}
		}
		
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < n; i++) {
			max = Math.max(dp[n-1][i], max);
		}
		
		System.out.println(max);
		
	}
	


}