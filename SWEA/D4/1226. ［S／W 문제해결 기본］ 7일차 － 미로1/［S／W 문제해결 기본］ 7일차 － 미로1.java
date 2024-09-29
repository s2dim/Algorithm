
import java.util.*;

public class Solution {
	
	static boolean[][] visited;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	static int ans;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		for (int t = 1; t <= 10; t++) {
			
			ans = 0;
			
			int arr[][] = new int[17][17];
			visited = new boolean[17][17];
			
			int startX = 0, startY = 0;
			int endX = 0, endY = 0;
			sc.nextInt();
			
			// 배열 입력 받기
			for (int i = 1; i <= 16; i++) {
				String str = sc.next();
				char[] c = str.toCharArray();
				for (int j = 1; j <= 16; j++) {
					int input = c[j-1] - '0';
					arr[i][j] = input;
					
					if (input == 2) {
						startX = i;
						startY = j;
					} else if (input == 3) {
						endX = i;
						endY = j;
					}
				}
			}
			DFS(startX, startY, endX, endY, arr);
			System.out.println("#" + t + " " + ans);
			
		} // tc
		
	}
	
	static void DFS(int x, int y, int endX, int endY, int[][] arr) {
		Stack<int[]> stack = new Stack<>();
		stack.add(new int[] {x, y});
		visited[x][y] = true;
		
		while (!stack.isEmpty()) {
			int[] curr = stack.pop();
			int currX = curr[0];
			int currY = curr[1];
			
			if (currX == endX && currY == endY) {
				ans = 1;
				return;
			}
			
			for (int d = 0; d < 4; d++) {
				int nx = currX + dx[d];
				int ny = currY + dy[d];
				
				if (nx > 0 && nx <= 16 && ny > 0 && ny <= 16 && !visited[nx][ny] && arr[nx][ny] != 1) {
					stack.add(new int[] {nx, ny});
					visited[nx][ny] = true;
				}
			}
			
		}
		
	}

}
