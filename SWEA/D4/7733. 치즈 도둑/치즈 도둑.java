
import java.util.*;

public class Solution {

	static int n;
	static int[][] arr;
	static boolean[][] visited;

	// 상 하 좌 우
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			n = sc.nextInt();

			arr = new int[n][n];

			// 배열 생성
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			int max = 1;
			int day = 1;

			// 면적이 다 사라질 때까지 반복 수행
			int all = n * n;
			while (all != 0) {
				visited = new boolean[n][n];
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (arr[i][j] == day) {
							arr[i][j] = 0;
							all--;
						}
					}
				}
				day++;

				int cnt = 0;
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (arr[i][j] > 0 && !visited[i][j]) {
							cnt++;
							bfs(i, j);
						}
					}
				}

				max = Math.max(max, cnt);
			}
			System.out.println("#" + t + " " + max);
		}
		sc.close();
	}

	static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] { x, y });
		visited[x][y] = true;

		while (!queue.isEmpty()) {
			int[] curr = queue.poll();
			int currX = curr[0];
			int currY = curr[1];

			for (int d = 0; d < 4; d++) {
				int nx = currX + dx[d];
				int ny = currY + dy[d];

				if (nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny] > 0 && !visited[nx][ny]) {
					queue.add(new int[] { nx, ny });
					visited[nx][ny] = true;
				}
			}
		}

	}
}
