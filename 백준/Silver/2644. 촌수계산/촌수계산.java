
import java.util.*;

public class Main {

	static Queue<Integer> queue;
	static boolean[] visited;
	static int[][] arr;
	static int n, m;
	static int person1, person2;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// 전체 사람의 수
		n = sc.nextInt();

		person1 = sc.nextInt();
		person2 = sc.nextInt();

		// 부모 자식 관계
		m = sc.nextInt();

		arr = new int[n + 1][n + 1];

		// 배열 생성 - m번의 관계 입력 받기
		for (int i = 0; i < m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();

			arr[a][b] = 1;
			arr[b][a] = 1;
		}

		queue = new LinkedList<>();
		visited = new boolean[n + 1];

		System.out.println(BFS());
	}

	static int BFS() {
		queue.offer(person1);
		visited[person1] = true;

		int cnt = 0;

		while (!queue.isEmpty()) {
			int size = queue.size();

			for (int s = 0; s < size; s++) {
				int a = queue.poll();

				if (a == person2) {
					return cnt;
				}

				for (int i = 1; i <= n; i++) {
					if (arr[a][i] == 1 && !visited[i]) {
						queue.offer(i);
						visited[i] = true;
					}
				}
			}
			cnt++;
		}
		return -1;
	}
}