import java.util.*;

public class Solution {

	static int n;
	static int[][] arr;
	static int day;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };
	static boolean[][] visited;
	static int cnt;
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			n = sc.nextInt();
			arr = new int[n][n];

			// 배열에 입력 받음
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			int max = 1;
			day = 1;
			while (day <= 100) {
				
				cnt = 0;
				visited = new boolean[n][n];
				
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (!visited[i][j] && arr[i][j] > day) {
							BFS(i, j);
							cnt++;
						}
					}
				}
				
				day++;
				max = Math.max(max, cnt);
			}
			
			System.out.println("#" + t + " " + max);
		}

	}

	static void BFS(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();

		queue.add(new int[] { x, y });
		visited[x][y] = true; 

		while (!queue.isEmpty()) {
			int[] curr = queue.poll();
			int currX = curr[0];
			int currY = curr[1];
//			cnt++;
			
			for (int d = 0; d < 4; d++) {
				int nx = currX + dx[d];
				int ny = currY + dy[d];

				if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] && arr[nx][ny] > day) {
					queue.add(new int[] { nx, ny });
					visited[nx][ny] = true;
				}
			}
		}
	}

}
