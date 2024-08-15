import java.util.*;

public class Main {
// 2024-08-15
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int sum = 0;

		for (int i = 1; i <= n; i++) {
			for (int j = i; j <= n / i; j++) {
				sum++;
			}
		}
		System.out.println(sum);

	}
}