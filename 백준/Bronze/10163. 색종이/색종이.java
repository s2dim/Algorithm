import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		int[][] arr = new int[1001][1001];

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		for (int i = 1; i <= N; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			int w = sc.nextInt();
			int h = sc.nextInt();

			for (int j = x; j < w + x; j++) {
				for (int k = y; k < h + y; k++) {
					arr[j][k] = i;

//					System.out.println(j + " " + k);
				}
			}
		}
		for (int i = 1; i <= N; i++) {
			int sum = 0;
			for (int a = 0; a < 1001; a++) {
				for (int b = 0; b < 1001; b++) {
					if (arr[a][b] == i) {
						sum++;
					}

				}

			}
			System.out.println(sum);
		}
	}
}