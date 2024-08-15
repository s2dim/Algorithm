import java.util.*;

public class Solution {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {

			int N = sc.nextInt();
			int M = sc.nextInt();

			int[][] arr = new int[N][M];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			int[] dx = { 0, 0, 1, -1 };
			int[] dy = { 1, -1, 0, 0 };

			int max = 0;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					int sum = arr[i][j];
					for (int d = 0; d < 4; d++) {
						for (int s = 1; s <= arr[i][j]; s++) {
							int nx = i + dx[d] * s;
							int ny = j + dy[d] * s;

							if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
								sum += arr[nx][ny];
							}
						}
					}
					max = Math.max(max, sum);
				}
			}

			System.out.println("#" + t + " " + max);
		}
	}
}
