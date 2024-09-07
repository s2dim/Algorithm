import java.util.*;

public class Main {

	static int[][][] dp = new int[101][101][101];

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		while (true) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();

			if (a == -1 && b == -1 && c == -1) {
				break;
			}
			System.out.printf("w(%d, %d, %d) = %d", a, b, c, w(a, b, c));
			System.out.println();
		}

	}

	static int w(int a, int b, int c) {
		if (a >= 0 && b >= 0 && c >=0 && dp[a][b][c] != 0)
			return dp[a][b][c];

		if (a <= 0 || b <= 0 || c <= 0)
			return 1;

		else if (a > 20 || b > 20 || c > 20)
			return dp[20][20][20] = w(20, 20, 20);

		else if (a < b && b < c)
			return dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);

		else
			return dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
	}

}
