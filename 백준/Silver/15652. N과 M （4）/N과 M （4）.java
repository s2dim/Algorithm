import java.util.Scanner;

public class Main {

	static int[] arr;
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		arr = new int[m];
		visited = new boolean[n];

		cal(n, m, 0, 0);
		System.out.println(sb);

	}

	static void cal(int n, int m, int start, int depth) {

		if (depth == m) {
			for (int i : arr) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
		} else {

			for (int i = start; i < n; i++) {

				arr[depth] = i + 1;
				cal(n, m, i , depth + 1);
			}
		}
	}

}