
import java.util.Scanner;

public class Main {

	static int n;
	static int[] podo;
	static int[] dp;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		podo = new int[n + 1];
		dp = new int[n + 1];

		for (int i = 1; i <= n; i++) {
			podo[i] = sc.nextInt();
		}

		dp[1] = podo[1];

		if (n >= 2)
			dp[2] = podo[1] + podo[2];

		if (n >= 3) {
			for (int i = 3; i <= n; i++) {
				dp[i] = Math.max(Math.max(dp[i - 2] + podo[i], dp[i - 3] + podo[i - 1] + podo[i]), dp[i - 1]);
			}
		}

		System.out.println(dp[n]);
	}

}
