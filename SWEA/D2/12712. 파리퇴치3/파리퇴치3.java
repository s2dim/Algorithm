import java.util.*;

public class Solution {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int M = sc.nextInt();

			int[][] arr = new int[N][N];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			int max = 0;

			// + 탐색
			int[] dx = { 1, -1, 0, 0 };
			int[] dy = { 0, 0, 1, -1 };

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int sum = arr[i][j];
					for (int d = 0; d < 4; d++) {
						for (int m = 1; m < M; m++) {
							int nx = i + dx[d] * m;
							int ny = j + dy[d] * m;

							if (nx >= 0 && nx < N && ny >= 0 && ny < N)
								sum += arr[nx][ny];
						}
					}

					max = Math.max(max, sum);
				}
			}

			// x 탐색
			int[] dx2 = { -1, -1, 1, 1 };
			int[] dy2 = { 1, -1, 1, -1 };

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int sum = arr[i][j];
					for (int d = 0; d < 4; d++) {
						for (int m = 1; m < M; m++) {
							int nx2 = i + dx2[d] * m;
							int ny2 = j + dy2[d] * m;

							if (nx2 >= 0 && nx2 < N && ny2 >= 0 && ny2 < N)
								sum += arr[nx2][ny2];
						}
					}
					max = Math.max(max, sum);
				}

			}
			System.out.println("#" + t + " " + max);
		}

	}
}
