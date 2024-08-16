import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int[][] arr = new int[101][101];

		int sum = 0;
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			for (int j = x; j < x + 10; j++) {
				for (int k = y; k < y + 10; k++) {
					arr[j][k] = '1';
				}
			}

		}
		
		for (int j = 1; j < 101; j++) {
			for (int k = 1; k < 101; k++) {
				if (arr[j][k] == '1')
					sum++;
			}
		}

		System.out.println(sum);
	}
}
