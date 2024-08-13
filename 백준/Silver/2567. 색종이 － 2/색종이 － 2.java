import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		// 100 * 100 배열 생성
		int[][] arr = new int[104][104];

		int sum = 0;

		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			for (int j = x; j < 10 + x; j++) {
				for (int k = y; k < 10 + y; k++) {
					arr[j][k] = 1;
				}
			}
		}

		for (int i = 1; i < 101; i++) {
			for (int j = 1; j < 101; j++) {
				if (arr[i][j] == 1) {
					if (arr[i][j + 1] == 0)
						sum++;
					if (arr[i][j - 1] == 0)
						sum++;
					if (arr[i + 1][j] == 0)
						sum++;
					if (arr[i - 1][j] == 0)
						sum++;
				}
			}
		}

		System.out.println(sum);
	}
}